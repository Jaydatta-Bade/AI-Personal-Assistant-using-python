"""
@author: jaydatta
"""

# Importing Required Libraries
import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia
import webbrowser
import os
import time
import subprocess
import pywhatkit
import pyjokes
import wolframalpha
import json
import requests

# Setting up the speech engine
# engine = pyttsx3.init('sapi5')
engine = pyttsx3.init()
voices = engine.getProperty('voices')
# engine.setProperty('voice', 'voices[0].id')  #male voice
engine.setProperty('voice', voices[1].id)  #female voice

# converts text to speech
def speak(text):
    engine.say(text)
    engine.runAndWait()


# Initiate a function to greet the user
def wishMe():
    hour = datetime.datetime.now().hour
    if hour >= 0 and hour < 12:
        speak("Hello,Good Morning")
        print("Hello,Good Morning")
    elif hour >= 12 and hour < 18:
        speak("Hello,Good Afternoon")
        print("Hello,Good Afternoon")
    else:
        speak("Hello,Good Evening")
        print("Hello,Good Evening")


# Setting up the command function
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)

        try:
            statement = r.recognize_google(audio, language='en-in')
            print(f"user said:{statement}\n")

        except Exception as e:
            speak("Pardon me, please say that again")
            return "None"
        return statement


print("Loading your AI personal assistant Alexa")
speak("Loading your AI personal assistant Alexa")
wishMe()

# the main function
if __name__ == '__main__':

    while True:
        speak("Tell me how can I help you now?")
        statement = takeCommand().lower()
        if statement == 0:
            continue

        if "good bye" in statement or "ok bye" in statement or "stop" in statement:
            speak('your personal assistant Alexa is shutting down,Good bye')
            print('your personal assistant Alexa is shutting down,Good bye')
        break

    # Task 1 -Fetching data from Wikipedia:
    if 'wikipedia' in statement or 'who is the' in statement or 'who the hake is' in statement:
        speak('Searching Wikipedia...')
        statement = statement.replace("wikipedia", "")
        results = wikipedia.summary(statement, sentences=3)
        speak("According to Wikipedia")
        print(results)
        speak(results)

    # Task 2 - Accessing the Web Browsers — Google Chrome, G - Mail and YouTube:
    elif 'play' in statement:
        song = statement.replace('play', '')
        speak('Playing' + song)
        pywhatkit.playonyt(song)

    elif 'open youtube' in statement:
        webbrowser.open_new_tab("https://www.youtube.com")
        speak("youtube is open now")
        time.sleep(5)

    elif 'open google' in statement:
        webbrowser.open_new_tab("https://www.google.com")
        speak("Google chrome is open now")
        time.sleep(5)

    elif 'open gmail' in statement:
        webbrowser.open_new_tab("gmail.com")
        speak("Google Mail open now")
        time.sleep(5)

    # Task 3 -Predicting time:
    elif 'time' in statement:
        strTime = datetime.datetime.now().strftime("%H:%M:%S")
        speak(f"the time is {strTime}")

    # Task 4 - To fetch latest news:
    elif 'news' in statement:
        news = webbrowser.open_new_tab("https://timesofindia.indiatimes.com/home/headlines")
        speak('Here are some headlines from the Times of India,Happy reading')
        time.sleep(6)

    # Task 5 - Searching data from web:
    elif 'search' in statement:
        statement = statement.replace("search", "")
        webbrowser.open_new_tab(statement)
        time.sleep(5)

    # Task 6 - Extra Features
    elif 'who are you' in statement or 'what can you do' in statement:
        speak('I am Alexa version 1 point O your personal assistant. I am programmed to minor tasks like'
              'opening youtube,google chrome, gmail and stackoverflow ,predict time,playing songs,search wikipedia,'
              'predict weather In different cities, get top headline news from times of india '
              'and you can ask me computational or geographical questions too!')

    elif 'joke' in statement:
        speak(pyjokes.get_joke())

    elif 'are you single' in statement:
        speak('I am in relationship with Google')

    elif "who made you" in statement or "who created you" in statement or "who discovered you" in statement:
        speak("I was built by Jaydatta")
        print("I was built by Jaydatta")
        

    # Task 7 - To turn off your PC:
    elif "log off" in statement or "sign out" in statement or "shut down" in statement:
        speak("Ok , your pc will log off in 10 sec make sure you exit from all applications")
        subprocess.call(["shutdown", "/l"])

time.sleep(3)
