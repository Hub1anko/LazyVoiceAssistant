#!/usr/bin/env python3

# NOTE: this example requires PyAudio because it uses the Microphone class

import speech_recognition as sr
import pyaudio
import numpy as np
import time
import os
import yaml
import wave
from playsound import playsound
from openwakeword import Model
from requests import post
from piper import PiperVoice

recognizer = sr.Recognizer()
wakewordmodel = Model(wakeword_models=['alexa'])

FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 16000
CHUNK = 1280
pyaudio = pyaudio.PyAudio()
mic_stream = pyaudio.open(format=FORMAT, channels=CHANNELS, rate=RATE, input=True, frames_per_buffer=CHUNK)
processor_device = 'cuda'


#set delay for activation
cooldown = 3 #seconds
activation_time = 0

def recognize(cooldown,activation_time):
	
	# Get audio
	audio = np.frombuffer(mic_stream.read(CHUNK), dtype=np.int16)

	prediction = wakewordmodel.predict(audio)
	#print(prediction)
	
	if prediction['alexa_v0.1.tflite'] >= 0.7 and (time.time() - activation_time) >= cooldown:
		playsound('voice/yesmaster.wav')
		
		# obtain audio from the microphone
		with sr.Microphone() as source:
			print("Say something!")
			audio = recognizer.listen(source)

			# recognize speech using whisper
			try:
				response = recognizer.recognize_whisper(audio, language="english", load_options=dict(device=processor_device))
				print("Whisper thinks you said: " + response)
				
				return response, time.time()
			except sr.UnknownValueError:
				print("Whisper could not understand audio")
			except sr.RequestError as e:
				print("Could not request results from Whisper")
	return None, 0
		
