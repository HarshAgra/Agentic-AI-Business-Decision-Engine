from utils.llm_client import call_llm

def market_agent(user_input):
    prompt = f"""
    You are a Market Analyst AI.

    Analyze the following business input and provide a market assessment.

    Input:
    {user_input}

    Tasks:
    1. Estimate demand level (Low/Medium/High)
    2. Analyze competition level
    3. Evaluate customer fit
    4. Give an opportunity score (1-10)

    Output strictly in this format:

    Demand:
    Competition:
    Customer Fit:
    Opportunity Score:
    Reason:
    """
    
    return call_llm(prompt)