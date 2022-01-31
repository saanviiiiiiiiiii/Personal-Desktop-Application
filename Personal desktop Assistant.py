#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 31 17:23:08 2022

@author: macbook
"""

from tkinter import *
import webbrowser
import speech_recognition as sr
import pyttsx3
from datetime import datetime
import subprocess

root = Tk()

root.geometry("500x500")
root.config(background="rose")


label = Label(root,text = "Welcome to your Personal Desktop Assistant",bg="dark pink",font=("Comforter",15,"bold" ))
label.place(rlex=0.5,rely=0.1,anchor=CENTER)

text_to_speech = pyttsx3.init()

def speak(audio):
    text_to_speech.say(audio)
    text_to_speech.runAndWait()
    
def r_audio():
    speech_recognisor= sr.Recognizer()
    speak("How can i help you..?")  
    with sr.Microphone() as source:
        audio=  speech_recognisor.listen(source)
        voice_data=''
        try:
            voice_data=  speech_recognisor.recognize_google(audio, language='en-in')
        except sr.UnknownValueError:
            print('Please repeat i did not get that')
            speak('Please repeat i did not get that')
            r_audio()
        respond(voice_data)
       
       
def respond(voice_data):
    print(voice_data)
    if "name" in voice_data:
        speak("My name is Jarvis")
        print('My name is Jarvis')
           
    if "time" in voice_data:
        speak("Current Time is")
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        speak(current_time)
        print(current_time)
           
    if "search" in voice_data:
        speak("Opening Google")
        print("Opening Google")
        webbrowser.get().open("https://google.com/")
           
    if "videos" in voice_data:
        speak("Opening YouTube")
        print("Opening YouTube")
        webbrowser.get().open("https://youtube.com/")
           
    if "text editor" in voice_data:
        speak("Opening the app")
        print("Opening the app")
        subprocess.Popen(["notepad.exe"])
        #for mac
        #subprocess.call(["/usr/bin/open", "/Applications/TextEdit.app"])        
       
btn= Button(root, text="Start", command=r_audio,bg="red3", fg="white", padx=10, pady=1,  font=("Arial",11, "bold"), relief=FLAT)
btn.place(relx=0.5,rely=0.5,anchor=CENTER)

root.mainloop()