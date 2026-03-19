from utils.llm_client import call_llm

def financial_agent(market_output, price, cost):
    prompt = f"""
    You are a Financial Analyst AI.

    Market Insights:
    {market_output}

    Selling Price: {price}
    Estimated Cost: {cost}

    Tasks:
    1. Estimate revenue level (Low/Medium/High)
    2. Estimate profit margin (%)
    3. Determine ROI level (Low/Medium/High)
    4. Decide financial viability (Good/Moderate/Poor)

    Output strictly in this format:

    Revenue:
    Profit Margin:
    ROI:
    Financial Viability:
    Reason:
    """
    
    return call_llm(prompt)