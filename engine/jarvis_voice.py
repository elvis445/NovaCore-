import speech_recognition as sr

def  listen_for_wake_word():
    r=sr.Recognizer()

    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)

        print("Listerning for wake world...")

        audio = r.listen(source)

        try:
            text =r.recognize_google(audio)
            return text.lower()
        
        except:
            return""
            