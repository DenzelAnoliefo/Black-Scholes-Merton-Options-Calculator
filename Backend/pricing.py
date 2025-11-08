import math
from scipy.stats import norm


# S -> Current price of the underlying asset
# K -> Strike Price
# t -> Time to Expiration (in years)
# r -> Risk-Free interest rate
# Q -> dividend Yield
# vol (σ) -> Volatility of the underlying asset's returns 

# 𝑁(⋅) -> The cumulative distribution function of the standard normal distribution
# d1 -> Intermediate calculation representing the standardized distance between the spot price and strike price, adjusted for drift and volatility
# d2 -> Intermediate calculation equal to d1 minus volatility scaled by the square root of time, representing the probability of the option expiring in-the-money

def d1(S, K, r, t, q, vol):
    return ((math.log((S/K))) + ((r - q + ((math.pow(vol, 2))/2))*t)) / (vol * (math.sqrt(t)))

def d2(S, K, r, t, q, vol):
    return (d1(S, K, r, t, q, vol) - (vol * math.sqrt(t)))

def callOption(S, K, r, t, q, vol):
    C = (S * (math.exp(-(q*t))) * norm.cdf(d1(S, K, r, t, q, vol))) - (K * (math.exp(-(r*t))) * norm.cdf(d2(S, K, r, t, q, vol)))
    return round(C, 2)

def putOption(S, K, r, t, q, vol):
    P = (K * (math.exp(-(r*t))) * norm.cdf(-(d2(S, K, r, t, q, vol)))) - (S * (math.exp(-(q*t))) * norm.cdf(-(d1(S, K, r, t, q, vol))))
    return round(P, 2)


