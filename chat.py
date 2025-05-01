import g4f
import pyttsx3

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[1].id)
engine.setProperty("rate", 200)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def GPT(message):
    try:
        response = g4f.ChatCompletion.create(
            model="gpt-4-32k-0613",
            provider=g4f.Provider.GPTalk,
            messages=[{"role": "user", "content": message}],
            stream=True
        )
        ms = ""
        for i in response:
            ms += i
            print(i, end="")
        speak(ms)
    except Exception as e:
        print(e)


# if __name__ == "__main__":
#     while True:
#         user_input = input("\nEnter String:\n")
#         if "Stop" in user_input:
#             break
#         else:
#             GPT(user_input)
speak("Hello My Name is AIGENT")
# import g4f
# flag = True

# import pyttsx3
# import speech_recognition
# import pyautogui
# import pywhatkit
# from datetime import datetime

# engine = pyttsx3.init("sapi5")
# voices = engine.getProperty("voices")
# engine.setProperty("voice",voices[1].id)
# engine.setProperty("rate",200)


# def speak(audio):
#     engine.say(audio)
#     engine.runAndWait()


# def GPT(message):
#     try:
#         respone = g4f.ChatCompletion.create(
#             model = "gpt-4-32k-0613",
#             provider=g4f.Provider.GPTalk,
#             messages=[{"role":"user","content":message}],
#             stream=True
#         )
#         ms=""
#         for i in respone:
#             ms+=i
#             print(i,end="")
#         speak(ms)
#     except Exception as e:
#         print(e)

# flag=True
# while(flag==True):
#     str = input("\nEnter String:\n")
#     if "Stop" in str:
#         break
#     else:
#         GPT(str)