from dotenv import load_dotenv
import os

load_dotenv()

HA_URL = os.getenv("HA_URL")
HA_TOKEN = os.getenv("HA_TOKEN")

OLLAMA_MODEL = "mistral"       # keep it light for fast responses

ENTITY_MAP = {
    "light.lamp": "switch.lamp",
    "light.lamp_led": "switch.lamp_led"
}

DEFAULT_LIGHT = "light.lamp"   # if user doesn't specify which lamp
