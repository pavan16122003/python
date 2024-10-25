import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser
import os

recognizer = sr.Recognizer()
engine = pyttsx3.init()


engine.setProperty('rate', 150) 
engine.setProperty('volume', 0.9)

def speak(text):
    engine.say(text)
    engine.runAndWait()

def take_command():
    try:
        with sr.Microphone() as source:
            print("Listening...")
            audio = recognizer.listen(source)
            command = recognizer.recognize_google(audio)
            print(f"User said: {command}\n")
            return command.lower()
    except sr.UnknownValueError:
        speak("Sorry, I did not catch that. Could you please repeat?")
        return "None"
    except sr.RequestError:
        speak("Sorry, the voice recognition service is unavailable.")
        return "None"

def execute_command(command):
    if 'time' in command:
        current_time = datetime.datetime.now().strftime("%H:%M")
        speak(f"The current time is {current_time}")
        
    elif 'open youtube' in command:
        speak("Opening YouTube")
        webbrowser.open("https://www.youtube.com")

    elif 'open google' in command:
        speak("Opening Google")
        webbrowser.open("https://www.google.com")

    elif 'exit' in command or 'stop' in command:
        speak("Goodbye!")
        exit()

    else:
        speak("I am not sure how to help with that.")


speak("How can I assist you today?")
while True:
    command = take_command()
    if command != "None":
        execute_command(command)
