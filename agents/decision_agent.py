from utils.llm_client import call_llm

def decision_agent(market, financial, risk):
    prompt = f"""
    You are a Strategy Head AI.

    Your job is to make a final business decision.

    Inputs:

    Market Analysis:
    {market}

    Financial Analysis:
    {financial}

    Risk Analysis:
    {risk}

    Decision Rules:
    - If ROI is Low OR Financial Viability is Poor, return Do Not Launch
    - If Risk Level is High, return Launch with Caution
    - If Demand is High AND ROI is High, return Launch

    Output strictly in this format:

    Final Decision:
    Confidence Level:
    Reason:
    """
    
    return call_llm(prompt)