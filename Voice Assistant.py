# Importing necessary libraries
import datetime
import os
import webbrowser

import pyttsx3
import speech_recognition as sr
import wikipedia

# Initializing pyttsx3 and setting the voice

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


# Function to make the assistant speak
def speak(audio):
    engine.say(audio)
    engine.runAndWait()


# Function to wish the user according to the time of the day
def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak(f"Good Morning The time is {hour} Hours")
    elif hour >= 12 and hour < 15:
        speak(f"Good afternoon The time is {hour} Hours")
    elif hour >= 15 and hour < 18:
        speak(f"Good Evening The time is {hour} Hours")
    elif hour >= 18 and hour < 24:
        speak(f"Good Night The time is {hour} Hours")
    speak("I am your personal Assistant. I was created by Kanak")


# Function to take input from the user's microphone
def takeCommand():
    # it takes microphone input from the user and returns string as output
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Speak Now")
        r.pause_threshold = 0.5
        audio = r.listen(source)
        print("Okay Got it")
    try:
        print("Understanding....")
        query = r.recognize_google(audio, language='en-in')
        print(f" You said {query}\n")
    except Exception as e1:
        # print(e1)
        print("Did not understood, Please say again")
        return "None"
    return query


if __name__ == "__main__":
    wishMe()
    query = takeCommand().lower()

    # Logics for executing the task
    if 'wikipedia' in query:
        query = query.replace("wikipedia", "")
        results = wikipedia.summary(query, sentences=2)
        speak(f"According to wikipedia {results}")

    elif 'open youtube' in query:
        webbrowser.open("youtube.com")

    elif 'open google' in query:
        webbrowser.open("google.com")

    elif 'play music' in query:
        music_dir = '<Path to your music directory>'
        songs = os.listdir(music_dir)
        print(songs)
        os.startfile(os.path.join(music_dir, songs[0]))
    elif 'the time' in query:
        strTime = datetime.datetime.now().strftime("%H:%M:%S")
        speak(f"the time is {strTime}")
    elif 'open brave' in query:
        codepath = "<Path to your Brave executable file>"
        os.startfile(codepath)
