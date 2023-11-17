#!/usr/bin/env python3

# NOTE: this example requires PyAudio because it uses the Microphone class

import speech_recognition as sr
import pyaudio
import numpy as np
import time
import torch
from playsound import playsound
from openwakeword import Model

class recognize:
    def __init__(self):
        self.recognizer = sr.Recognizer()
        self.wakewordmodel = Model(wakeword_models=['alexa'])

        self.FORMAT = pyaudio.paInt16
        self.CHANNELS = 1
        self.RATE = 16000
        self.CHUNK = 1280
        self.pyaudio = pyaudio.PyAudio()
        self.mic_stream = self.pyaudio.open(format=self.FORMAT, channels=self.CHANNELS, rate=self.RATE, input=True, frames_per_buffer=self.CHUNK)
        if torch.cuda.is_available():
            self.processor_device = 'cuda'
        else:
            self.processor_device = 'cpu'

        #set delay for activation
        self.cooldown = 3 #seconds
        self.activation_time = 0
        self.whisperModel = "base" # possible: tiny, base, small, medium, large

    def recognize(self):
        # Get audio
        self.audio = np.frombuffer(self.mic_stream.read(self.CHUNK), dtype=np.int16)

        self.prediction = self.wakewordmodel.predict(self.audio)
        #print(prediction)
	
        if self.prediction['alexa_v0.1.tflite'] >= 0.7 and (time.time() - self.activation_time) >= self.cooldown:
            playsound('voice/yesmaster.wav')
            # obtain audio from the microphone
            with sr.Microphone() as source:
                print("Say something!")
                self.audio = self.recognizer.listen(source)

                # recognize speech using whisper
                try:
                    self.response = self.recognizer.recognize_whisper(self.audio, model=self.whisperModel, language="english", load_options=dict(device=self.processor_device))
                    print("Whisper thinks you said: " + self.response)
                    self.activation_time = time.time()
                    return self.response
                except sr.UnknownValueError:
                    print("Whisper could not understand audio")
                except sr.RequestError as e:
                    print("Could not request results from Whisper")
                self.activation_time = time.time()