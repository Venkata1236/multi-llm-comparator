import requests
import os
from dotenv import load_dotenv

load_dotenv()

HF_TOKEN = os.getenv("HF_TOKEN")
print("TOKEN:", HF_TOKEN)

MODEL = "mistralai/Mistral-7B-Instruct-v0.2"
API_URL = f"https://router.huggingface.co/hf-inference/models/{MODEL}"

headers = {
    "Authorization": f"Bearer {HF_TOKEN}",
    "Content-Type": "application/json"
}

def query_model(prompt):
    payload = {
        "inputs": f"<s>[INST] {prompt} [/INST]",
        "parameters": {
            "max_new_tokens": 300,
            "temperature": 0.3
        }
    }

    response = requests.post(API_URL, headers=headers, json=payload)
    return response.json()

if __name__ == "__main__":
    result = query_model("What is RAG in LLM?")
    print(result)