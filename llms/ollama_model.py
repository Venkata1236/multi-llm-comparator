import requests

def get_ollama_response(prompt):
    response = requests.post(
        "http://localhost:11434/api/generate",
        json={
            "model": "llama3",
            "prompt": f"Answer accurately. If unsure, say you don't know.\n\nQuestion: {prompt}",
            "stream": False
        }
    )

    return response.json()["response"]