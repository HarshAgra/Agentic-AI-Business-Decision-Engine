# 🧠 Agentic AI Business Decision Engine

A multi-agent AI system that simulates real-world business decision-making using Azure OpenAI and Streamlit.

---

## 🚀 Project Overview

This project implements an **Agentic AI Workflow**, where multiple AI agents collaborate to analyze a business problem and generate a final strategic decision.

Instead of using a single LLM, the system uses specialized agents:
- 📊 Market Analyst
- 💰 Financial Analyst
- ⚠️ Risk Analyst
- 🧠 Decision Agent

Each agent performs a specific role, and their outputs are combined to generate a final recommendation.

---

## ⚙️ How It Works

```text
User Input
   ↓
Market Agent
   ↓
Financial Agent + Risk Agent
   ↓
Decision Agent
   ↓
Final Recommendation
