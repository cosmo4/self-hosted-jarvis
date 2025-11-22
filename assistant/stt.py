from faster_whisper import WhisperModel

model = WhisperModel("base", device="cpu")

def transcribe(audio):
    segments, _ = model.transcribe(audio)
    text = "".join(seg.text for seg in segments).strip()
    return text
