import webbrowser
import time
import pyautogui as gui
from speak import speak
from listen import listen

def map(location):
    # speak("sir ! tell me the location you want to see in map")
    webbrowser.open("https://www.google.com/maps/@16.3524328,79.8664982,16196013m/data=!3m1!1e3")
    time.sleep(8)
    gui.write(location)
    speak("searching.")

    gui.press("enter")
    speak(f"here is the {location} in earth")

map("satna,mp")