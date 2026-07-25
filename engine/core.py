import os
import webbrowser
from brain.thinker import think
from internet.web_engine import internet_status
from engine.voice import speak,listen

def run_novacore():
    speak("NovaCore is Online")
    print(internet_status())
    while True:
        user=input("You:").lower()

        if user.lower()== "voice" :
            user = listen()
            if user == "":
                continue

        if user =="":
            continue

        if user.lower() == "exit":
            print("NovaCore: Shutting down...")
            speak("Shutting down")
            break
        
        
        elif user.lower().startswith("search"):
            query = user[7:].strip()

        if query:
            webbrowser.open(f"https://www.google.com/search?q="+query)
            print(f"NovaCore:Searching Google for"+query)
            speak(f"Searching Google for"+query)

        else:
            speak("What do you want me to search for?")
            continue

        if user.lower() == "open notepad":
            os.system("notepad")
            speak("Opening Notepad")
            continue

        elif user.lower() == "open calculator":
            os.system("calc")
            speak("Opening Calculator")
            continue

        elif user.lower() == "open paint":
            os.system("mspaint")
            speak("Opening Paint")
            continue
        
        answer = think(user)
        print(f"NovaCore:",answer)
        speak(answer)

if __name__ == "__main__":
        run_novacore()