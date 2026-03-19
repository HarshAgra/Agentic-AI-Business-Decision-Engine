from utils.llm_client import call_llm

def risk_agent(market_output):
    prompt = f"""
    You are a Risk Analyst AI.

    Market Insights:
    {market_output}

    Tasks:
    1. Determine risk level (Low/Medium/High)
    2. Identify key risks
    3. Suggest mitigation strategies

    Output strictly in this format:

    Risk Level:
    Key Risks:
    Mitigation:
    Reason:
    """
    
    return call_llm(prompt)