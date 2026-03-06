
import requests, json

# 🔑 PUT YOUR OPENROUTER API KEY HERE
OPENROUTER_API_KEY = "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"

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

        return r.json()['choices'][0]['message']['content']

    except Exception as e:
        return str(e)
