import datetime
from speak import speak
from playsound import playsound


def set_alarm(time_str):
    try:
        alarm_time = datetime.datetime.strptime(time_str, "%I:%M %p").time()
        current_time = datetime.datetime.now().time()

        while current_time < alarm_time:
            current_time = datetime.datetime.now().time()

        speak("I apologize for the disturbance but this is an alam alert")


    except ValueError:
        print("sir, this is Invalid time format. Please use the format like '8:00 AM'.")
        speak("sir , this is Invalid time format. Please use the format like '8:00 AM'.")

