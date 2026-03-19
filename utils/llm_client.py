import os
from openai import AzureOpenAI
from dotenv import load_dotenv

load_dotenv()

client = AzureOpenAI(
    api_key=st.secrets["AZURE_OPENAI_API_KEY"],
    api_version="2024-02-15-preview",
    azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT")
)

def call_llm(prompt):
    response = client.chat.completions.create(
        model=st.secrets["AZURE_OPENAI_DEPLOYMENT"],
        messages=[
            {"role": "system", "content": prompt}
        ],
        temperature=0.3
    )
    
    return response.choices[0].message.content
