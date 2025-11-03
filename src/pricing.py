import math
from scipy.stats import norm

# S -> Current price of the underlying asset
# K -> Strike Price
# t -> Time to Expiration (in years)
# r -> Risk-Free interest rate
# Q -> dividend Yield
# vol -> Volatility of the underlying asset's returns (σ)

# 𝑁(⋅) -> The cumulative distribution function of the standard normal distribution
# d1 ->
# d2 -> 


def d1(S, K, r, t, q, vol):
    return ((math.log((S/K))) + ((r - q + ((math.pow(vol, 2))/2))*t)) / (vol * (math.sqrt(t)))

def d2(S, K, r, t, q, vol):
    return (d1(S, K, r, t, q, vol) - (vol * math.sqrt(t)))

def callOption(S, K, r, t, q, vol):
    C = (S * (math.exp(-(q*t))) * norm.cdf(d1(S, K, r, t, q, vol))) - (K * (math.exp(-(r*t))) * norm.cdf(d2(S, K, r, t, q, vol)))
    return C

def putOption(S, K, r, t, q, vol):
    P = (K * (math.exp(-(r*t))) * norm.cdf(-(d2(S, K, r, t, q, vol)))) - (S * (math.exp(-(q*t))) * norm.cdf(-(d1(S, K, r, t, q, vol))))
    return P


print(callOption(100, 100, 0.05, 0.25, 0, 0.3))
print(putOption(100, 100, 0.05, 0.25, 0, 0.3))
print(d1(100, 100, 0.05, 0.25, 0, 0.3))
print(d2(100, 100, 0.05, 0.25, 0, 0.3))
