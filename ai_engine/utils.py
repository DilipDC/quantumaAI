
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
