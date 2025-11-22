import subprocess
import tempfile
import sounddevice as sd
import soundfile as sf

def speak(text, model="en_US-ryan-high"):
    with tempfile.NamedTemporaryFile(suffix=".wav") as tmp:
        subprocess.run([
            "piper", "--model", model, "--output_file", tmp.name
        ], input=text.encode("utf8"))

        audio, sr = sf.read(tmp.name)
        sd.play(audio, sr)
        sd.wait()
