import pyttsx3
import threading
import speech_recognition as sr

engine=pyttsx3.init()
engine.setProperty('rate',170)

voices = engine.getProperty("voices")
if len(voices)> 0:
    engine.setProperty("voice",voices[0].id)

def _speak_worker(text):
    engine.say(text)
    engine.runAndWait()

def speak(text):
    print("NovaCore:",text)
    threading.Thread(target=_speak_worker,args=(text,),daemon=True).start()

def listen():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source,duration=0.5)
        
    try:
        audio=r.listen(source,timeout=5,phrase_time_limit=6)
        text = r.recognize_google(audio)

        return text.lower()
    except:
        return"I didn't understand"
        

