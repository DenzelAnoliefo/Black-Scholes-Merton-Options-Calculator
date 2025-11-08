# Black-Scholes-Merton Options Calculator

![Options Calculator](https://user-images.githubusercontent.com/placeholder-image.png)  
*A simple, interactive tool to calculate European call and put option prices using the Black-Scholes-Merton model.*

---

## Table of Contents
- [Overview](#overview)  
- [About Black-Scholes-Merton](#about-black-scholes-merton)  
- [How the Model Works](#how-the-model-works)  
- [Project Structure](#project-structure)  
- [Features](#features)  
- [Installation and Running](#installation-and-running)  
- [Usage](#usage)  
- [Legacy Fullstack Version](#legacy-fullstack-version)  
- [Future Work](#future-work)  

---

## Overview
This project provides a user-friendly web interface to calculate European call and put option prices using the **Black-Scholes-Merton model**. The app allows users to input key option parameters and instantly see the results.  

It was originally built using React + FastAPI but is now implemented in **Streamlit**, making it easier to deploy and share globally.  

---

## About Black-Scholes-Merton
The Black-Scholes-Merton model is a **mathematical framework for pricing European-style options**. Developed in 1973 by Fischer Black, Myron Scholes, and Robert Merton, it provides a formula to determine the **fair price** of an option based on several variables:  

1. **Current Stock Price (S)** – The price of the underlying asset today.  
2. **Strike Price (K)** – The price at which the option can be exercised.  
3. **Time to Maturity (t)** – Time in years until the option expires.  
4. **Risk-Free Interest Rate (r)** – The theoretical return of a risk-free investment, e.g., government bonds.  
5. **Dividend Yield (q)** – The expected annual dividend payout of the stock.  
6. **Volatility (σ or vol)** – The standard deviation of the stock’s returns, representing its risk.  

---

## How the Model Works
The formula for a **European call option** (C) and **put option** (P) is:

\[
d_1 = \frac{\ln(S / K) + (r - q + 0.5 \cdot \sigma^2) \cdot t}{\sigma \cdot \sqrt{t}}
\]

\[
d_2 = d_1 - \sigma \cdot \sqrt{t}
\]

\[
C = S e^{-q t} N(d_1) - K e^{-r t} N(d_2)
\]

\[
P = K e^{-r t} N(-d_2) - S e^{-q t} N(-d_1)
\]

Where \(N(\cdot)\) is the cumulative distribution function of the standard normal distribution.  

This model allows traders and analysts to estimate **fair option prices** and make informed decisions in financial markets.  

---

## Project Structure

