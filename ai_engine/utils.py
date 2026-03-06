
import requests, json, os

OPENROUTER_API_KEY = os.getenv("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")

def get_quantum_response(prompt):

    headers = {
        "Authorization": f"Bearer {OPENROUTER_API_KEY}",
        "Content-Type": "application/json"
    }

    data = {
        "model": "google/gemini-2.0-flash-001",
        "messages": [
            {"role":"user","content":prompt}
        ]
    }

    try:
        r = requests.post(
            "https://openrouter.ai/api/v1/chat/completions",
            headers=headers,
            data=json.dumps(data)
        )

        response = r.json()
        return response["choices"][0]["message"]["content"]

    except Exception as e:
        return f"AI connection error: {str(e)}"
