# Black-Scholes-Merton Options Calculator

[![Streamlit App](https://img.shields.io/badge/Live-App-brightgreen)](https://black-scholes-options-calculator.streamlit.app)
[![Python](https://img.shields.io/badge/Python-3.13-blue)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.30-orange)](https://streamlit.io/)

> A simple, interactive tool to calculate European call and put option prices using the Black-Scholes-Merton model.

---

## Table of Contents
- [Overview](#overview)  
- [About Black-Scholes-Merton-Formula](#about-black-scholes-merton-formula)  
- [How the Model Works](#how-the-model-works)   
- [Features](#features)  
- [Demo](#demo)  
- [Usage](#usage)  
- [Legacy Fullstack Version](#legacy-fullstack-version)  
- [Future Work](#future-work)  
- [Created By](#created-by)  

---

## Overview
This project provides a **user-friendly web interface** to calculate European call and put option prices using the **Black-Scholes-Merton model**.  

It was originally built using React + FastAPI but is now implemented in **Streamlit**, making it easier to deploy and share globally.  

---

## About Black-Scholes-Merton-Formula
The Black-Scholes-Merton model is a **mathematical framework for pricing European-style options**. Developed in 1973 by Fischer Black, Myron Scholes, and Robert Merton, it provides a formula to determine the **fair price** of an option based on several variables:  

The Black-Scholes formula arises from **modeling the stock price as a stochastic process** and solving a partial differential equation (PDE).

1. **Stock Price Dynamics**
The stock price S(t) is assumed to follow **geometric Brownian motion**:

dS = μS dt + σS dW  

Where:
- μ is the expected return of the stock,
- σ is the volatility,
- dW is a Wiener process (random noise term).

This models the stock price as continuously fluctuating with both a deterministic drift (μ) and a stochastic component (σ).

2. **Construct a Risk-Free Portfolio**
We consider a portfolio Π consisting of:
- A long position in the option (V), and
- A short position in Δ shares of the stock (Δ = ∂V/∂S).

The portfolio is:  
Π = V - Δ S  

Using **Ito’s Lemma** on V(S,t) and substituting dS gives dΠ.  
We choose Δ = ∂V/∂S to **eliminate the stochastic part** (the dW term), making the portfolio risk-free.

3. **The Black-Scholes PDE**
For a risk-free portfolio, the return must equal the risk-free interest rate r:

dΠ = r Π dt  

Substituting and simplifying gives the **Black-Scholes PDE**:

∂V/∂t + 0.5 σ² S² ∂²V/∂S² + (r - q) S ∂V/∂S - r V = 0  

- This PDE governs how the option price V(S,t) evolves over time.
- q is included if the stock pays a continuous dividend yield.

4. **Boundary Conditions**
- For a **call option**, at expiration t=T: V(S,T) = max(S-K, 0)
- For a **put option**, at expiration t=T: V(S,T) = max(K-S, 0)

5. **Solving the PDE**
Using **change of variables** and techniques from heat equation theory, the PDE can be solved in closed form, giving the familiar formulas:

d1 = [ln(S/K) + (r - q + 0.5 σ²) t] / (σ √t)  
d2 = d1 - σ √t  

Call: C = S e^(-q t) N(d1) - K e^(-r t) N(d2)  
Put:  P = K e^(-r t) N(-d2) - S e^(-q t) N(-d1)

6. **Intuition Behind d1 and d2**
- d1 represents the **risk-adjusted probability** that the option will end up in-the-money.  
- d2 is d1 minus the **volatility adjustment**, giving the expected log-distance from the strike price under risk-neutral measure.  
- N(d1) and N(d2) are cumulative probabilities under the **risk-neutral distribution**, which is why we can discount by r and q to get present value.

In short:
- The Black-Scholes formula comes from **hedging away risk**, turning a stochastic process into a deterministic PDE, and solving it using probabilistic methods.  
- It combines **stock dynamics, time value, volatility, and risk-free discounting** into a single elegant formula for fair option pricing.
 

---

## How the Model Works
Formulas for **European call (C) and put (P) options**:  

d1 = [ ln(S / K) + (r - q + 0.5 * σ^2) * t ] / (σ * sqrt(t))

d2 = d1 - σ * sqrt(t)

Call Option Price (C) = S * e^(-q * t) * N(d1) - K * e^(-r * t) * N(d2)

Put Option Price (P) = K * e^(-r * t) * N(-d2) - S * e^(-q * t) * N(-d1)

Where:
S = Current price of the underlying stock  

K = Strike price of the option  

t = Time to maturity in years  

r = Risk-free interest rate  

q = Dividend yield of the stock  

σ = Volatility of the stock’s returns  

N(x) = Cumulative distribution function of the standard normal distribution

---

## Features
- **Interactive inputs**: Users can input:
  - Current stock price ($S)  
  - Strike price ($K)  
  - Time to maturity (t) in years  
  - Risk-free interest rate (r) as a percentage  
  - Dividend yield (q) as a percentage  
  - Volatility (σ) as a percentage  
- **Instant calculations**: Get both **call** and **put** prices with a single click.  
- **Visually clean interface** with Streamlit.  
- **Preserved legacy code** in case you want to explore React + FastAPI.  

---

## Demo
Check out the live demo here:  
[🔗 Black-Scholes-Merton Options Calculator](https://black-scholes-options-calculator.streamlit.app)

---

## Usage

1. Enter the required values in the input boxes.  
2. Click **“Calculate Options Prices”**.  
3. View the calculated **Call** and **Put** option prices.  

**Notes:**  
- Rates (`r`, `q`, `vol`) are percentages (e.g., 5 for 5%).  
- Stock prices use a **$** prefix automatically.  
- Time is in **years**.  

---

## Legacy Fullstack Version

The folder `legacy_fullstack/` contains the **previous React + FastAPI implementation**:  
- `frontend/` – React app for inputs and results.  
- `backend/` – FastAPI backend for calculations.  

Preserved for **learning and reference**.  

---

## Future Work

- Add **interactive graphs** for option prices vs. stock price or volatility.  
- Include **Greeks**: Delta, Gamma, Theta, Vega, Rho.  
- Deploy globally without setup.  

---

## Created By

**Denzel Anoliefo** – [GitHub](https://github.com/DenzelAnoliefo) | [Live App](https://black-scholes-options-calculator.streamlit.app)


