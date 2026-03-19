from agents.market_agent import market_agent
from agents.financial_agent import financial_agent
from agents.risk_agent import risk_agent
from agents.decision_agent import decision_agent

def run_workflow(user_input, price, cost):

    market_output = market_agent(user_input)

    financial_output = financial_agent(market_output, price, cost)

    risk_output = risk_agent(market_output)

    decision_output = decision_agent(
        market_output,
        financial_output,
        risk_output
    )

    return decision_output