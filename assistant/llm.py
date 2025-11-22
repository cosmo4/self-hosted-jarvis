import requests
import json
import re
from config import OLLAMA_MODEL

def extract_json(text):
    # Match the first {...} JSON object in the text
    match = re.search(r"\{.*?\}", text, flags=re.DOTALL)
    if not match:
        raise ValueError("No JSON object found in LLM output.")

    json_str = match.group(0)
    return json.loads(json_str)

def ask_llm(user_text):
    url = "http://localhost:11434/api/chat"

    payload = {
        "model": OLLAMA_MODEL,
        "messages": [
            {
                "role": "system",
                "content": (
                    "You are a home automation assistant. "
                    "Understand the user's intent and output JSON only. "
                    "Supported actions: turn_on, turn_off. "
                    "If no entity is mentioned, assume 'light.lamp'."
                )
            },
            {
                "role": "user",
                "content": user_text
            }
        ],
        "format": {
            "type": "object",
            "properties": {
                "action": {"type": "string"},
                "entity": {"type": "string"},
            },
            "required": ["action"]
        },
        "stream": False
    }

    r = requests.post(url, json=payload)
    r.raise_for_status()
    response_data = r.json()
    print("LLM Response:", response_data)
    content = response_data["message"]["content"]
    print("LLM Response Content:", content)

    return content

# import requests
# import json

# def ask_llm(prompt):
#     response = requests.post(
#         "http://localhost:11434/api/chat",
#         json={
#             "model": "mistral",
#             "messages": [{"role": "user", "content": prompt}],
#             "format": {
#                 "type": "object",
#                 "properties": {
#                     "action": {"type": "string"},
#                     "entity": {"type": "string"}
#                 },
#                 "required": ["action"]
#             }
#         }
#     )
#     return response.json()["message"]["content"]
