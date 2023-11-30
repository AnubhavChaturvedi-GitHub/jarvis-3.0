import pyttsx3
import threading

def speak(text):
    def speak_thread(text):
        engine = pyttsx3.init()
        
        voices = engine.getProperty('voices')
        engine.setProperty('voice', voices[0].id)
        engine.setProperty('rate', 192)
        engine.setProperty('pitch', 800)
        engine.setProperty('volume', 100)  # Adjust this value to control the volume
        engine.say(text)
        engine.runAndWait()

    speak_thread = threading.Thread(target=speak_thread, args=(text,))
    speak_thread.start()
    speak_thread.join()

# speak("Allow me to introduce myself ! ,I am Jarvis, a virtual artificial intelligence and I am here to assist you with the variety of tasks which best I can ! 24 hours a day, 7 days a week, Importing all preferences and herm interfaces ,all operation is fully completed sir ")


def speak_f(text):
    def speak_thread(text):
        engine = pyttsx3.init()

        voices = engine.getProperty('voices')
        engine.setProperty('voice', voices[1].id)
        engine.setProperty('rate', 192)
        engine.setProperty('pitch', 800)
        engine.setProperty('volume', 100)  # Adjust this value to control the volume
        engine.say(text)
        engine.runAndWait()

    speak_thread = threading.Thread(target=speak_thread, args=(text,))
    speak_thread.start()
    speak_thread.join()

# speak_f("Hello sir! Friday is always happy to assist you")