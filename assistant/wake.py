from openwakeword import Model
import sounddevice as sd
import numpy as np

model = Model(wakeword_models=["hey_jarvis"])  # change for yours

def wait_for_wake_word():
    print("Listening for wake word...")

    def callback(indata, frames, time, status):
        pcm = indata[:, 0].astype(np.float32)
        if model.predict(pcm):
            raise sd.CallbackStop

    with sd.InputStream(callback=callback, channels=1, samplerate=16000):
        try:
            sd.sleep(99999999)
        except sd.CallbackStop:
            print("Wake word detected!")
            return
