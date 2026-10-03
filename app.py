#configuration and setup
import streamlit as st
import numpy as np

st.set_page_config(
    page_title="M-Pesa Churn Predictor",
    page_icon="📱",
    layout = "centered"
)

st.title("📱M-Pesa Customer Churn Prediction Engine")
st.markdown("This interactive web utility uses our trained ** Logistic Regression model ** to prdict customer defection based on transaction behaviour.") 
st.markdown("---")

#interactive sidebar inputs
st.sidebar.header("Customer Profile Inputs")
age=st.sidebar.slider("Customer Age",18,70,30,1)
frequency=st.sidebar.slider("Transaction Frequency (count)",0,30,5,1)
monetary_value=st.sidebar.number_input("Total Transaction Volume(KES)",0,500000,15000,500)
recency_days = st.sidebar.slider("Recency (Days Since Last Transaction)",0,90,10,1)

#prediction logic and executive output
def predict_churn(freq, rec, mon, ag):
    z = 0.08 * rec - 0.35 * freq - 0.00002 * mon + 0.01 * (ag - 30) - 1.5
    return 1 / (1 + np.exp(-z))

churn_probability = predict_churn(frequency, recency_days, monetary_value, age)

col1, col2 = st.columns(2)

with col1:
    st.subheader("Customer Metrics Summary")
    st.write(f"* **Age:** {age} years")
    st.write(f"* **Frequency:** {frequency} transactions")
    st.write(f"* **Volume:** KES {monetary_value:,.2f}")
    st.write(f"* **Recency:** {recency_days} days inactive")

with col2:
    st.subheader("Prediction Result")
    st.metric(label="Calculated Churn Probability", value=f"{churn_probability * 100:.1f}%")

    st.markdown("---")

if churn_probability > 0.5:
    st.error("🚨 **HIGH RISK DETECTED:** Customer showing indicators of defection. **Action:** Trigger promotional retention incentives.")
else:
    st.success("🟢 **LOW RISK / LOOSELY ANCHORED:** Customer is healthy and active. No retention spend required.")