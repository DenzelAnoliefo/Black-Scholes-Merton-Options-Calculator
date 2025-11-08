# Black-Scholes-Merton Options Calculator

![Options Calculator](https://user-images.githubusercontent.com/placeholder-image.png)  

[![Streamlit App](https://img.shields.io/badge/Live-App-brightgreen)](https://black-scholes-options-calculator.streamlit.app)
[![Python](https://img.shields.io/badge/Python-3.13-blue)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.30-orange)](https://streamlit.io/)

> A simple, interactive tool to calculate European call and put option prices using the Black-Scholes-Merton model.

---

## Table of Contents
- [Overview](#overview)  
- [About Black-Scholes-Merton](#about-black-scholes-merton)  
- [How the Model Works](#how-the-model-works)  
- [Project Structure](#project-structure)  
- [Features](#features)  
- [Demo](#demo)  
- [Installation and Running](#installation-and-running)  
- [Usage](#usage)  
- [Legacy Fullstack Version](#legacy-fullstack-version)  
- [Future Work](#future-work)  
- [Created By](#created-by)  

---

## Overview
This project provides a **user-friendly web interface** to calculate European call and put option prices using the **Black-Scholes-Merton model**.  

It was originally built using React + FastAPI but is now implemented in **Streamlit**, making it easier to deploy and share globally.  

---

## About Black-Scholes-Merton
The Black-Scholes-Merton model is a **mathematical framework for pricing European-style options**. Developed in 1973 by Fischer Black, Myron Scholes, and Robert Merton, it provides a formula to determine the **fair price** of an option based on several variables:  

1. **Current Stock Price (S)** – Price of the underlying asset today.  
2. **Strike Price (K)** – Price at which the option can be exercised.  
3. **Time to Maturity (t)** – Time in years until the option expires.  
4. **Risk-Free Interest Rate (r)** – Return of a risk-free investment.  
5. **Dividend Yield (q)** – Expected annual dividend payout.  
6. **Volatility (σ)** – Standard deviation of the stock’s returns.  

---

## How the Model Works
Formulas for **European call (C) and put (P) options**:

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

---

## Project Structure

Black-Scholes-Merton-Options-Calculator/
│
├── streamlit_app/
│ ├── app.py # Main Streamlit app
│ ├── pricing.py # Option calculation functions
│ └── requirements.txt # Dependencies for Streamlit app
│
├── legacy_fullstack/
│ ├── frontend/ # React frontend (previous implementation)
│ └── backend/ # FastAPI backend (previous implementation)
│
├── README.md # This file
└── .gitignore


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


