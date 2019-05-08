import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import time
import smtplib
import config

# Install below package for mac user
# pip install pyobjc
# pip install speechRecognition
# install gcc before install pyaudio
# brew update
# brew install portaudio
# pip install pyaudio

# set Your machine voice 
engine = pyttsx3.init()
voices = engine.getProperty('voices')
#print(voices[0].id)
engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour <=12:
        speak("Good Morning")
    elif hour >=12 and hour<18:
        speak("Good Afternoon")
    else:
        speak("Good Evening")

    speak("What can i do for you sir")

def takeComand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listining...!")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing....!")
        query = r.recognize_google(audio, language = 'en-in')
        print((f"User said: {query}\n"))

    except Exception as e:
        print("Sorry please say it again..")
        return "None"
    return query

def sendEmail(to, content):
    # For sending mail from your email id You must turn on
    # "Less secure app access" from your google setting
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login(config.email, config.password)
    server.sendmail('ijreat@gmail.com', to, content)
    server.close()


if __name__ == "__main__":
    wishMe()
    #print('Welcome')
    #query = 'email to'
    while True:
        query = takeComand().lower()
        if 'hello' in query:
            speak('Hi')
        # wikipedia
        elif 'wikipedia' in query:
            speak('Searching Wikipedia')
            query = query.replace("wikipedia", "")
            result = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(result)
            speak(result)
        elif 'open youtube' in query:
            webbrowser.open("www.youtube.com")

        elif 'open google' in query:
            webbrowser.open("www.google.com")
        
        elif 'open youtube' in query:
            webbrowser.open("www.youtube.com")
        
        elif 'play music' in query:
            music_dir = '/users/shubham/Jarvis/music'
            song = os.listdir(music_dir)
            print(song)
            a = '/users/shubham/Jarvis/music/' + song[1]
            os.system("open " + a)
        
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")

        elif 'email to' in query:
            # You can import your google contact
            if 'shubham' in query:
                try:
                    speak("What should I say?")
                    content = takeCommand()
                    #content = 'Hi'
                    to = "shubham@gmail.com"
                    sendEmail(to, content)
                    speak("Email has been sent!")
                except Exception as e:
                    print(e)
                    speak("I am not able to send this email, sorry")
            elif 'Ram' in query:
                 try:
                    speak("What should I say?")
                    content = takeCommand()
                    #content = 'Hi'
                    to = "ram@gmail.com"
                    sendEmail(to, content)
                    speak("Email has been sent!")
                except Exception as e:
                    print(e)
                    speak("I am not able to send this email, sorry")

        elif 'goodbye' in query:
            break

   



