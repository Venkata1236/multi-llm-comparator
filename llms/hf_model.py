import requests
from config.settings import HF_TOKEN

API_URL = "https://api-inference.huggingface.co/models/mistralai/Mistral-7B-Instruct"

headers = {"Authorization": f"Bearer {HF_TOKEN}"}

def get_hf_response(prompt):
    payload = {
        "inputs": prompt,
        "parameters": {"max_new_tokens": 300}
    }

    response = requests.post(API_URL, headers=headers, json=payload)
    data = response.json()

    if isinstance(data, list):
        return data[0]["generated_text"]
    
    elif "error" in data:
        return f"HF Error: {data['error']}"
    
    else:
        return str(data)