import speech_recognition as sr
import os
import threading

# Function to listen for speech
def listen():
    recognizer = sr.Recognizer()
    recognizer.dynamic_energy_threshold = False
    recognizer.energy_threshold = 4000  # Adjust this threshold based on your environment

    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source)


        while True:
            print("Listening....", end='', flush=True)
            try:
                audio = recognizer.listen(source, timeout=None)
                print("\rRecognizing...   ", end='', flush=True)
                recognized_text = recognizer.recognize_google(audio).lower()  # Convert to lowercase
                if recognized_text:
                    print("\rZENo : " + recognized_text)
            except sr.UnknownValueError:
                recognized_text = ""  # Set recognized_text to an empty string in case of error
            finally:
                print("\r", end='', flush=True)  # Erase "Listening...." and "Recognizing..."
                os.system('cls' if os.name == 'nt' else 'clear')  # Clear the console after recognition

# Start listening thread
            listen_thread = threading.Thread(target=listen)
            listen_thread.start()
            print_thread = threading.Thread(target=print_loop)
            print_thread.start()

            listen_thread.join()
            print_thread.join()


# Function to continuously print
def print_loop():
    while True:
        print("", end='', flush=True)

# Start printing thread
listen()