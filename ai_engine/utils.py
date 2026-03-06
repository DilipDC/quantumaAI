
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
