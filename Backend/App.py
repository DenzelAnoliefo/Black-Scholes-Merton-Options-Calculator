import streamlit as st
from pricing import callOption, putOption  # or just define them here

st.title("Black-Scholes Options Calculator")

S = st.number_input("Current stock price ($)")
K = st.number_input("Strike price ($)")
t = st.number_input("Time to maturity (Yrs)")
r = st.number_input("Risk-free interest rate (%)")
q = st.number_input("Dividend Yield (%)")
vol = st.number_input("Volatility (%)")

operation = st.selectbox("Select Option Type", ["Call Option", "Put Option"])

if st.button("Calculate"):
    if operation == "Call Option":
        result = callOption(S, K, r/100, t, q/100, vol/100)
    else:
        result = putOption(S, K, r/100, t, q/100, vol/100)

    st.write(f"{operation} Value: ${result}")
