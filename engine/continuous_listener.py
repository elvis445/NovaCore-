from engine.jarvis_voice import listen_for_wake_word
from brain.thinker import think
from engine.voice import speak


def start_jarvis():

    while True:
        text = listen_for_wake_word()
        if "novacore" in text:

            speak("YesB Elvis,I am listening")

            from engine.jarvis_voice import listen_for_wake_word

            command = listen_for_wake_word()

            answer = think(command)

            speak(answer)
