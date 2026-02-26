# Black-Scholes-Merton Options Calculator

A simple, interactive web application to calculate European call and put option prices.

[![Streamlit App](https://img.shields.io/badge/Live-App-brightgreen)](https://black-scholes-options-calculator.streamlit.app)
[![Python](https://img.shields.io/badge/Python-3.13-blue)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.30-orange)](https://streamlit.io/)

## Overview
This project provides a clean, user-friendly web interface for options pricing. Originally built as a full-stack application using React and FastAPI, it is currently implemented in Streamlit to streamline deployment and provide a cohesive interactive experience.

## Tech Stack
* **Current:** Python, Streamlit
* **Legacy Full-Stack Version:** React (Frontend), FastAPI (Backend)

## Features
* **Interactive UI:** Users can easily input parameters like stock price, strike price, and volatility.
* **Real-time Processing:** Calculates and displays call and put prices instantly.
* **Legacy Architecture:** The `legacy_fullstack/` directory preserves the original React and FastAPI implementation for reference.

## Usage
1. Visit the [live app](https://black-scholes-options-calculator.streamlit.app).
2. Enter the required parameters (Stock Price, Strike Price, Time to Maturity, Risk-Free Rate, Dividend Yield, and Volatility).
3. Click **"Calculate Options Prices"** to view the results instantly.

## Future Work
* Implement interactive data visualizations for option prices.
* Integrate additional metrics (the Greeks).

## Author
**Denzel Anoliefo** – [GitHub](https://github.com/DenzelAnoliefo) | [Live App](https://black-scholes-options-calculator.streamlit.app)


