import streamlit as st
from workflows.main_workflow import run_workflow

st.set_page_config(page_title="Agentic Decision Engine", layout="centered")

st.title("🧠 Agentic AI Decision Engine")
st.write("Get AI-powered decision recommendations using multi-agent workflow")

# User Inputs
product = st.text_input("Product Name")
market = st.text_input("Target Market")
segment = st.text_input("Customer Segment")

price = st.number_input("Selling Price", value=10000)
cost = st.number_input("Estimated Cost", value=7000)

# Button
if st.button("Analyze"):

    user_input = f"""
    Product: {product}
    Market: {market}
    Segment: {segment}
    """

    with st.spinner("Analyzing with AI agents..."):
        result = run_workflow(user_input, price, cost)

    st.success("Analysis Complete")

    st.subheader("📊 Final Decision")
    st.write(result)