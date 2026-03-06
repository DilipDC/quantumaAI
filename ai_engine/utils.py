import requests
import json
import os

OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")

def get_quantum_response(prompt):

    url = "https://openrouter.ai/api/v1/chat/completions"

    headers = {
        "Authorization": f"Bearer {OPENROUTER_API_KEY}",
        "Content-Type": "application/json"
    }

    data = {
        "model": "deepseek/deepseek-chat",
        "messages": [
            {"role": "user", "content": prompt}
        ]
    }

    try:
        r = requests.post(url, headers=headers, data=json.dumps(data))
        response = r.json()

        print(response)  # debug

        if "choices" in response:
            return response["choices"][0]["message"]["content"]

        return "AI returned unexpected response."

    except Exception as e:
        return f"Error connecting to AI: {str(e)}"
