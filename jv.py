# -*- coding: utf-8 -*-
"""
Created on Sat Jan  9 17:01:43 2021

@author: arora
"""
import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
from googlesearch import search
import requests,sys,webbrowser,bs4
engine = pyttsx3.init('sapi5')
voices= engine.getProperty('voices')
#print(voices[1].id)
engine.setProperty('voices', voices[1].id)
def speak(audio):
    engine.say(audio)
    engine.runAndWait()
def wishme():
    hour= int(datetime.datetime.now().hour)
    if hour>=0 and hour<=12:
        speak('good morning')
    elif hour>=12 and hour<18:
        speak('good afternoon')
    else:
        speak('good evening')
    speak('hi, my name is JV how would i help you?')
def takecommand():
    #takes voice input and string as output
    r= sr.Recognizer()
    with sr.Microphone()as source:
        print('listening.....')
        r.pause_threshold=1
        r.energy_threshold=500
        audio=r.listen(source)
        
        
    try:
        print('recognizing....')
        query= r.recognize_google(audio, language='en-in')
        print(f'user said,{query}\n')
    except Exception as e:
        #print(e)
        speak('say that again please')
        return 'none'
    return query
    pass

if __name__== "__main__":
    #speak("Nice work")
    wishme()
    while True:
       query=takecommand().lower()
       if 'wikipedia' in query:
           speak('searching....')
           query= query.replace('wikipedia','')
           results= wikipedia.summary(query,sentences=2)
           speak('accordig to wikipedia')
           print(results)
           speak(results)
           speak('any other command for me?')
           out= takecommand().lower()
           if('quit' in out or 'no' in out ):
               speak('Have a nice day, now i am taking your leave')
               break
           else:
               continue
       elif'open youtube' in query:
           webbrowser.open('youtube.com')
           speak('any other command for me?')
           out= takecommand().lower()
           if('quit' in out or 'no' in out ):
               speak('Have a nice day, now i am taking your leave')
               break
           else:
               continue
       elif 'open learn portal' in query:
           webbrowser.open("learn.niituniversity.in")
           speak('any other command for me?')
           out= takecommand().lower()
           if('quit' in out or 'no' in out ):
               speak('Have a nice day, now i am taking your leave')
               break
           else:
               continue
       elif 'open spotify' in query:
           spotify_path= 'C:\\Users\\arora\\AppData\\Local\\Microsoft\\WindowsApps\\SpotifyAB.SpotifyMusic_zpdnekdrzrea0\\Spotify.exe'
           os.startfile(spotify_path)
           speak('any other command for me?')
           out= takecommand().lower()
           if('quit' in out or 'no' in out ):
               speak('Have a nice day, now i am taking your leave') 
               break
           else:
               continue
       elif 'open word' in query:
           word_path="C:\\Program Files\\Microsoft Office\\root\\Office16\\WINWORD.EXE"
           os.startfile(word_path)
           speak('any other command for me?')
           out= takecommand().lower()
           if('quit' in out or 'no' in out ):
               speak('Have a nice day, now i am taking your leave')
               break
           else:
               continue
       elif 'open game' in query:
            metro_path= "C:\Riot Games\Riot Client\RiotClientServices.exe"
            os.startfile(metro_path)
            speak('any other command for me?')
            out= takecommand().lower()
            if('quit' in out or 'no' in out ):
               speak('Have a nice day, now i am taking your leave')
               break
       elif 'search' in query:
          
           query=query.replace('search','')
           url=[]
           for i in search(query,num_results=5):
               url.append(i)
           print(url[0])
           speak('opening URL')
           webbrowser.open(url[0])
           speak('any other command for me?')
           out= takecommand().lower()
           if('quit' in out or 'no' in out ):
               break
       elif 'time' in query:
         strTime= datetime.datetime.now().strftime('%H:%M')
         speak(f"the time is {strTime}")  
       elif 'bye' or 'jv quit' or 'jv leave' in query:
           speak('Have a nice day, now i am taking your leave')
           break           
       
           