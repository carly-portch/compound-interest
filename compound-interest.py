import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

def compound_interest(principal, monthly_contribution, rate, years):
    rate = rate / 100 / 12  # Convert annual rate to monthly
    months = years * 12
    balance = principal
    values = []
    
    for month in range(1, months + 1):
        balance = balance * (1 + rate) + monthly_contribution
        if month % 12 == 0:  # Store yearly values
            values.append(balance)
    
    return values

def simple_savings_values(principal, monthly_contribution, years):
    values = []
    for year in range(1, years + 1):
        values.append(principal + (monthly_contribution * 12 * year))
    return values

st.sidebar.header("Input your numbers here:")
initial_principal = st.sidebar.number_input("Initial Investment ($)", value=1000, step=100)
monthly_contribution = st.sidebar.number_input("Monthly Contribution ($)", value=200, step=10)
risk_free_rate = 7  # Assume 7% annual return

years = st.sidebar.slider("Investment Duration (Years)", 1, 50, 30)

total_values = compound_interest(initial_principal, monthly_contribution, risk_free_rate, years)
simple_savings_values_list = simple_savings_values(initial_principal, monthly_contribution, years)

years_range = list(range(1, years + 1))

final_value = total_values[-1] if total_values else 0
no_investment_value = simple_savings_values_list[-1] if simple_savings_values_list else 0

st.subheader(f"After {years} years, your investment would be worth: ${final_value:,.2f}")
st.subheader(f"If you saved without investing, you would have: ${no_investment_value:,.2f}")

fig, ax = plt.subplots()
ax.plot(years_range, total_values, label="Investment Growth", linestyle="-", marker="o")
ax.plot(years_range, simple_savings_values_list, label="Savings Without Investment", linestyle="--", marker="s", color='red')
ax.set_xlabel("Years")
ax.set_ylabel("Total Value ($)")
ax.set_title("The Power of Compound Interest")
ax.legend()
st.pyplot(fig)

st.markdown("""
**Disclaimer:** This calculator is for informational purposes only and is based on assumed annual stock market returns of 7% with monthly compounding. Actual returns may vary due to market fluctuations, fees, inflation, and other factors. This is not financial advice—please consult a financial professional before making investment decisions.
""")
