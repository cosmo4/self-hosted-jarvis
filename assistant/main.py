import sounddevice as sd
import numpy as np
import json
import traceback

from stt import transcribe
from llm import ask_llm, extract_json
from ha_client import HomeAssistantAPI
from config import HA_URL, HA_TOKEN, ENTITY_MAP, DEFAULT_LIGHT

ha = HomeAssistantAPI(HA_URL, HA_TOKEN)

def record_audio(seconds=5, samplerate=16000):
    print("Listening for command...")
    audio = sd.rec(int(seconds * samplerate), samplerate=samplerate, channels=1, device=4, dtype="float32")
    sd.wait()
    return audio[:,0]

while True:
    input("\nPress ENTER to speak...")

    # 1. Record audio
    audio_data = record_audio()

    # 2. STT
    text = transcribe(audio_data)
    print("You said:", text)

    if not text:
        print("Didn't hear anything.")
        continue

    # 3. LLM decides action
    try:
        raw = ask_llm(text)
        print("LLM Raw Output:", raw)

        parsed = extract_json(raw)
        print("LLM Parsed Output:", parsed)
        
    except Exception as e:
        print("LLM Error:", e)
        print("\nFull traceback:")
        traceback.print_exc()
        continue

    action = parsed["action"]
    raw_entity = parsed.get("entity", DEFAULT_LIGHT)

    # Translate "light.*" to actual switch.*
    entity = ENTITY_MAP.get(raw_entity, raw_entity)

    # 4. Send to Home Assistant
    domain = entity.split(".")[0]
    service = "turn_on" if action == "turn_on" else "turn_off"

    result = ha.call_service(domain, service, {"entity_id": entity})
    print("Home Assistant result:", result)

    print(f"Task complete: {entity} → {service}")


# from stt import transcribe
# from llm import ask_llm
# from ha_client import HomeAssistantAPI
# from config import HA_URL, HA_TOKEN
# import sounddevice as sd
# import numpy as np
# import json

# ha = HomeAssistantAPI(HA_URL, HA_TOKEN)

# def record_audio(seconds=5, samplerate=16000):
#     print("Listening...")
#     audio = sd.rec(int(seconds * samplerate), samplerate=samplerate, channels=1, dtype='float32')
#     sd.wait()
#     return audio[:,0]

# while True:
#     input("Press ENTER to give a voice command...")

#     audio = record_audio()
#     text = transcribe(audio)
#     print("You said:", text)

#     llm_output = ask_llm(text)
#     print("LLM response:", llm_output)

#     data = json.loads(llm_output)
#     action = data["action"]
#     entity = data.get("entity", "light.living_room_lamp")

#     domain = entity.split(".")[0]
#     service = "turn_on" if action == "turn_on" else "turn_off"

#     result = ha.call_service(domain, service, {"entity_id": entity})
#     print("Service result:", result)
