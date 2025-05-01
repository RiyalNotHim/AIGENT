import pyttsx3
import speech_recognition
import pyautogui
import pywhatkit
from datetime import datetime

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice",voices[1].id)
engine.setProperty("rate",200)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

speak("hello i'm the AIGENT")