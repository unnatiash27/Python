import speech_recognition as sr
import webbrowser
import pyttsx3
import musicLibrary
import requests
from openai import OpenAI


ecognizer = sr.Recognizer()
engine=pyttsx3.init()
newsapi="<newsapi>"

def speak(text):
    engine.say(text)
    engine.runAndWait()

def aiProcess(command):
    client = OpenAI(api_key="<api-key>",
    )

    completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are a virtual assistant named jarvis skilled in general tasks like Alexa and Google Cloud. Give short responses please"},
        {"role": "user", "content": command}
    ]
    )
    return completion.choices[0].message.content

def processCommand(c):
    if "open google" in c.lower():
        webbrowser.open("http://google.com")
    elif "open facebook" in c.lower():
        webbrowser.open("http://facebook.com")
    elif "open youtube" in c.lower():
        webbrowser.open("http://youtube.com")
    elif "open linkedin" in c.lower():
        webbrowser.open("http://linkedin.com")
    elif c.lower().startswith("play"):
        song=c.lower().split(" ")[1]
        link=musicLibrary.music[song]
        webbrowser.open(link)
    elif "news"in c.lower() :
        r=requests.get(f"https://newsapi.org/v2/top-headlines?country=in&apiKey={newsapi}")
        if r.status_code==200:
            data=r.json()
            articles=data.get('articles',[])
            for article in articles:
                speak(article['title'])
    else:
        output=aiProcess(c)
        speak(output)
        # openAI
    # print(c)
    # pass

if __name__=="__main__":
    speak("Initializing Jarvis.....")
    # listen for wake word-Jarvis
    while True:
        r=sr.Recognizer()
        
        print("Recognizing...")

        try:
            with sr.Microphone()as source:
                print("Listening....")
                audio=r.listen(source, timeout=4, phrase_time_limit=2)
            word=r.recognize_google(audio)
            if(word.lower() == "jarvis"):
                speak("Yes")
                with sr.Microphone()as source:
                    print("Jarvis Active!")
                    audio=r.listen(source)
                    command=r.recognize_google(audio)

                    processCommand(command)

        except Exception as e:
                print("Error;{0}".format(e))

