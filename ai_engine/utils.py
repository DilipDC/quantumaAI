import requests
import json
import os

# Get API key from Render Environment Variables
OPENROUTER_API_KEY = os.getenv("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")

def get_quantum_response(prompt, deep_mode=False):

    enhanced_prompt = f"Improve and answer this request clearly: {prompt}"

    if deep_mode:
        enhanced_prompt += " Provide deeper technical reasoning."

    headers = {
        "Authorization": f"Bearer {OPENROUTER_API_KEY}",
        "Content-Type": "application/json"
    }

    data = {
        "model": "google/gemini-2.0-flash-001",
        "messages": [
            {"role": "user", "content": enhanced_prompt}
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
        return f"Error connecting to AI: {str(e)}"
