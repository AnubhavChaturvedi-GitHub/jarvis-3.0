import speech_recognition as sr
import cv2
import numpy as np
import pyautogui
from listen import listen


# Function to control the volume based on voice commands
def control_volume():
     while True:
            command = listen().lower()
            try:

                if "increase volume" in command:
                    pyautogui.press("volumeup")
                    pyautogui.press("volumeup")
                    pyautogui.press("volumeup")
                    pyautogui.press("volumeup")
                    pyautogui.press("volumeup")
                    print("Volume increased.")
                elif "decrease volume" in command:
                    pyautogui.press("volumedown")
                    pyautogui.press("volumedown")
                    pyautogui.press("volumedown")
                    pyautogui.press("volumedown")
                    pyautogui.press("volumedown")
                    print("Volume decreased.")
                elif "mute" in command:
                    pyautogui.press("volumemute")
                    print("Volume muted.")
                elif "exit" in command:
                    print("Exiting volume control.")
                else:
                    print("Command not recognized.")

            except sr.UnknownValueError:
                print("Speech Recognition could not understand audio.")
            except sr.RequestError as e:
                print(f"Could not request results from Google Speech Recognition service; {e}")


if __name__ == "__main__":
    control_volume()
