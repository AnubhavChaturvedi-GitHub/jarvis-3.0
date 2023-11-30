import datetime
from datetime import date
from speak import speak
import random
from wed import temp_outside
from playsound import playsound

today = date.today()
formatted_date = today.strftime("%d %b %Y")

nowx = datetime.datetime.now()

def random_morning_greeting():
    good_morning_wish = [
        "Good to see you again, sir. Very good morning, sir!",
        "Hello, sir! Wishing you a wonderful morning!",
        "Top of the morning to you, sir!",
        "Rise and shine, sir! Good morning!",
        "A bright and cheerful morning, sir!",
        "Greetings, sir! Have a fantastic morning!",
        "Wishing you a day filled with positivity, sir!",
        "Good morning, sir! May your day be great!",
        "Hello, sir! Starting the day with a warm greeting!",
        "A pleasant morning to you, sir!"
    ]
    selected_greeting = random.choice(good_morning_wish)
    current_time = datetime.datetime.now().strftime("%I:%M %p")
    speak(f"{selected_greeting}, the time is {current_time}")
    temp_outside()


def random_afternoon_greeting():
    good_afternoon_wish = [
        "Good afternoon, sir! Hope you're having a great day!",
        "Hello, sir! Wishing you a pleasant afternoon!",
        "Afternoon greetings, sir! May your day continue to be wonderful!",
        "Good day, sir! Sending positive vibes your way this afternoon!",
        "Hello, sir! Enjoying the afternoon sunshine, I hope!",
        "Good afternoon, sir! Keep up the fantastic work!",
        "Afternoon, sir! Wishing you success in all your endeavors!",
        "Greetings, sir! Hope your afternoon is as bright as your morning!",
        "Hello, sir! Just checking in to wish you a fantastic afternoon!",
        "Good afternoon, sir! Keep smiling and shining!"
    ]
    selected_greeting = random.choice(good_afternoon_wish)
    speak(selected_greeting)

def random_evening_greeting():
    good_evening_wish = [
        "Good evening, sir! Wishing you a peaceful and relaxing evening!",
        "Hello, sir! As the day winds down, may your evening be filled with joy!",
        "Evening greetings, sir! Take a moment to unwind and enjoy the evening!",
        "Good evening, sir! Reflect on the achievements of the day!",
        "Hello, sir! Wishing you a pleasant and serene evening!",
        "Evening, sir! May your night be as calm as the evening sky!",
        "Good evening, sir! Take a break and enjoy the beauty of the evening!",
        "Greetings, sir! Hope you have a delightful evening ahead!",
        "Hello, sir! Evening is a time to recharge and relax. Enjoy!",
        "Good evening, sir! May the night bring you peace and happiness!"
    ]
    selected_greeting = random.choice(good_evening_wish)
    speak(selected_greeting)


def jarvis_live():
    jarvis_live= [
        "Good day, sir/madam. How may I assist you today?"
        "At your service, just like a well-programmed butler."
        "Sir/Madam, your wish is my command."
        "Welcome back, boss. What can I do for you?"
        "Hello there! Ready for some technological magic?"
        "Greetings, [Your Name]. I trust you had a satisfactory absence. How may I be of service?"
        "Good to see you again, [Your Name]. What can I do to make your day extraordinary?"
        "Ah, the prodigal [Your Name] returns. How may I facilitate your plans today?"
        "I'm here and ready to serve, just like clockwork."
        "Hello, [Your Name]. What's on the agenda for today? More world domination or a chill day?"
    ]
    selected_greeting = random.choice(jarvis_live)
    speak(selected_greeting)

def wish():
    if nowx.hour < 12:
        random_morning_greeting()
    elif nowx.hour < 16:
        random_afternoon_greeting()
    else:
        random_evening_greeting()

