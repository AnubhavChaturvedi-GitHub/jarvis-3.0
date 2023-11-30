from Study_Time_Activated import study_time_setup
from playmusic import play_music_on_youtube
from open_operation import open_chat_GPT
from open_operation import open_chrome
from open_operation import open_facebook
from open_operation import open_googleclassroom_default
from open_operation import open_insta
from open_operation import open_telegram
from open_operation import open_Whatsapp
from open_operation import open_youtube
from open_operation import open_ytstudio
from battery import battery_alert
from battery import battey_persentage
from battery import check_plugin_status
from Youtube import good_night_setup
from Youtube import shut_down
from alarm_alt import set_alarm
from brain import search_brain
from datetime import datetime
from listen import listen
from speak import speak
import pyautogui as gui
from wish import wish
from openapp import open_control_panel
from openapp import open_edge
from openapp import open_linkedin
from openapp import open_microsoft_store
from openapp import open_wpsoffice
from openapp import open_pycharm
from openapp import open_whatsapp
from openapp import open_settings
from openapp import open_spotify
from openapp import open_paint
from openapp import open_photos
from openapp import open_word
from openapp import open_powerpoind
from openapp import open_pdfreader
import threading
from brain import load_qa_data
import os
from search import *
# from sendmessageonWA import Send_massege_on_Whatsapp

operation_dict = { 
    "open wps office": open_wpsoffice,
    "open python code editor": open_pycharm,
    "open business whatsapp": open_whatsapp,
    "open linkedin app": open_linkedin,
    "open browser": open_edge,
    "open spotify": open_spotify,
    "open settings": open_settings,
    "open Microsoft store": open_microsoft_store,
    "open paint": open_paint,
    "open photos": open_photos,
    "open ms word": open_word,
    "open powerpoint": open_powerpoind,
    "open pdf reader": open_pdfreader,
    "open control panel": open_control_panel,
    # Add more entries for other operations
}
qa_file_path = "C:\\Users\\vlogp\\Documents\\Jarvis\\qna_logbook.txt"
qa_dict = load_qa_data(qa_file_path)
wish()


def main():

    while True:
        text = listen().lower()

        if "what is the time" in text or "is the time" in text:
            current_time = datetime.now().strftime("%I:%M %p")
            print("Current Time:", current_time)
            time = "sir,the Time is :", current_time
            speak(time)

        elif text.startswith(("who is ", "what is ", "how to ", "what are", " show me", "tell me", "tell me about")):
            search_brain(text)
            continue

        elif "set alarm" in text or "set alarm a.m." in text or "set alarm p.m." in text or "jarvis set alarm" in text:
            text = text.replace("jarvis", "")
            text = text.replace("set alarm", "")
            text = text.replace(" ", "")
            text = text.replace("a.m.", " AM")
            text = text.replace("p.m.", " PM")
            speak(f"Well done sir, you have successfully set an alarm using Jarvis for {text}")
            threading.Timer(5, set_alarm, args=(text,)).start()
            threading.Timer(5, main).start()

        elif "open youtube studio" in text or "open YouTube studio" in text or "open youtube studio" in text or "open youtube studio" in text:
            open_ytstudio()

        elif "open google classroom" in text or " open Google classroom" in text or "open google classroom" in text or "open google classroom" in text:
            open_googleclassroom_default()

        elif "open facebook" in text or "open Facebook" in text or "open faceboo" in text or "open facebo" in text:
            open_facebook()

        elif "check battery percentage" in text or "check battery" in text or "check battey persent" in text or "check battery" in text:
            battey_persentage()

        elif "open youtube" in text or "open tube in text" in text:
            open_youtube()

        elif "open telegram" in text or "open telegram app" in text:
            open_telegram()

        elif "open instagram" in text or "open insta" in text:
            open_insta()

        elif "open chrome" in text or "open google" in text:
            open_chrome()

        elif "open whatsapp" in text or "open what'sapp" in text or "open whats app" in text or "open what's app" in text:
            open_Whatsapp()

        elif "open chat GPT" in text or "open chatgpt" in text or "open chat gpt" in text or "open chat gpt" in text:
            open_chat_GPT()

        elif "close" in text or "close this" in text or "close tab" in text:
            speak("closing...")
            gui.hotkey('alt', 'f4')

        elif text in qa_dict:
            ans = qa_dict[text]
            speak_thread = threading.Thread(target=speak, args=(ans,))
            speak_thread.start()
            speak_thread.join()

        elif "shutdown" in text or "shut down" in text:
            shut_down()

        elif "good morning" in text or "good evening" in text:
            wish()

        elif "minimise" in text or "minimise the window" in text:
            gui.hotkey('win', 'd')

        elif "play music" in text or "play music on youtube" in text:
            speak("Sir, which song do you want to play?")
            song_name = listen().lower()
            play_music_on_youtube(song_name)

        elif "send message on whatsapp" in text:
            Send_massege_on_Whatsapp()

        elif "show me the youtube chanel progress" in text or "show me the youtube progress" in text:
            speak("sure sir, which chanel do you want to check?")
            text = listen().lower()
            if "nethyfun" in text:
                NetHyFun_Count()
            elif "night conspiracy" in text or "nightconspiracy" in text or "night conspiracy" in text or "night conspiracy" in text or "nightconspiracy" in text:
                Night_Conspiracy_Count()
            elif "nethytoons" in text or "nethy toons" in text or "net hy toons" in text or "net high tunes" in text:
                NetHyToons_Count()
            elif "royal free music" in text or "royal free music ncs" in text or "royal free music ncs" in text:
                Royal_Free_Music_NCS_Count()
                continue

        elif "jarvis" in text or "jarv" in text or "jarvi" in text:
            search_brain(text)
            continue
        elif "good night" in text:
            good_night_setup()

        elif "i want to study" in text or "study time" in text or "study setup activated" in text:
            study_time_setup()

        elif text in operation_dict:
            operation_dict[text]()

        elif "search in google" in text or "search on google" in text:
            text = text.replace("search in google","")
            text = text.replace("search on google","")
            search_on_google(text)

        elif "search in youtube" in text or "search on youtube" in text:
            text = text.replace("search in google","")
            text = text.replace("search on google","")
            search_on_youtube(text)

        elif "search in chatgpt" in text or "search on chatgpt" in text  or "search in chat gpt" in text or "search on chat gpt" in text or "ask to friday" in text or "ask friday" in text:
            text = text.replace("search in chatgpt","")
            text = text.replace("search on chatgpt","")
            text = text.replace("search in chat gpt", "")
            text = text.replace("search on chat gpt", "")
            text = text.replace("ask to friday", "")
            text = text.replace("ask friday", "")

            search_on_chatgpt(text)

if __name__ == '__main__':
    thread1 = threading.Thread(target=battery_alert)
    thread2 = threading.Thread(target=main)
    thread3 = threading.Thread(target=check_plugin_status)    
    thread1.start()
    thread2.start()
    thread3.start()
    thread1.join()
    thread2.join()
    thread3.join()
