import pyttsx3
import speech_recognition
import pyautogui
import pywhatkit
import random as rm
from datetime import datetime

engine = pyttsx3.init("sapi5") #this is used to change the voice
voices = engine.getProperty("voices")
engine.setProperty("voice",voices[1].id)
engine.setProperty("rate",160) #Setting the Rate

def speak(audio): # this Function is Used to speak
    engine.say(audio)
    engine.runAndWait()

speak('''Now me to introduce myself, im AIGENT. The Virtual Artificial Intelligence, and i'm here you to assist you 
                        the varity of task the best i can . 24 hours the day, 7 days of week. importing all preferences to hub interface, the system is now
                        Fully operational''')