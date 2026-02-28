import requests
import os
from dotenv import load_dotenv

load_dotenv()

HF_TOKEN = os.getenv("HF_TOKEN")

API_URL = "https://api-inference.huggingface.co/models/meta-llama/Llama-3-8B-Instruct"

headers = {
    "Authorization": f"Bearer {HF_TOKEN}"
}

def query_model(prompt):
    payload = {
        "inputs": prompt,
        "parameters": {
            "max_new_tokens": 200,
            "temperature": 0.3
        }
    }

    response = requests.post(API_URL, headers=headers, json=payload)
    return response.json()

if __name__ == "__main__":
    result = query_model("What is RAG in LLM?")
    print(result)