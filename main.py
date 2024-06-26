import speech_recognition as sr
import webbrowser
import pyttsx3
import musicLibrary
import requests
from openai import OpenAI
import time

recognizer=sr.Recognizer()
engine = pyttsx3.init()
newsapi="Your_News_API_Key"

def speak(text):
    engine.say(text)
    engine.runAndWait()

def processCommand(c):
    if "open google" in c.lower():
        webbrowser.open("https://google.com")
    elif "open youtube" in c.lower():
        webbrowser.open("https://youtube.com")
    elif "open facebook" in c.lower():
        webbrowser.open("https://facebook.com")
    elif "open linkedin" in c.lower():
        webbrowser.open("https://linkedin.com")
    elif "open instagram" in c.lower():
        webbrowser.open("https://instagram.com")
    elif "open gmail" in c.lower():
        webbrowser.open("https://gmail.com")

    elif c.lower().startswith("play"):
        song=c.lower().split(" ")[1]
        link=musicLibrary.music[song]
        webbrowser.open(link)

    elif "news" in c.lower():
        r=requests.get(f"https://newsapi.org/v2/top-headlines?country=us&apiKey={newsapi}")
        if r.status_code==200:
            # Parse the JSON response
            data=r.json()

            # Extract the articles
            articles=data.get('articles')

            # Print the headlines
            for article in articles:
                speak(article['title'])

    else:
        output=aiProcess(command)
        print(output)            


def aiProcess(command): # Paid API
    # pip install openai
    # if you saved the key under a different environment variable name, you can do something like:
    client = OpenAI(api_key="Your_OpenAI_API_Key")

    completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are a virtual assistant named JARVIS, skilled in coding."},
        {"role": "user", "content": command}
    ]
    )

    print(completion.choices[0].message)
                



if __name__=="__main__":
    speak("Welcome Home Sir! Initializing Jarvis...")
    while True:
        # Listen for the wake word "Arcage"
        # obtain audio from the microphone
        r = sr.Recognizer()


        # recognize speech using Google
        try:
            with sr.Microphone() as source:
                print("Listening...")
                audio = r.listen(source,timeout=2,phrase_time_limit=1)
                
            word=r.recognize_google(audio)
            # print(word)

            if word.lower()=="jarvis":
                speak("Yeah Sir! Activating Javis...")
                # Listen for command
                with sr.Microphone() as source:
                    print("Activating Javis...")
                    audio = r.listen(source)
                    command=r.recognize_google(audio)

                    processCommand(command)

        except Exception as e:
            print("Try Again :)")