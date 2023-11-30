import pywhatkit as kit
from speak import speak
from listen import listen
import random


def Send_massege_on_Whatsapp():
    # Get the name of the contact

    speak("who do you want to massege sir")
    contact_name = listen().lower()

    if contact_name == "papa":
        contact_name = "+918226098666"

    elif contact_name == "girlfriend":
        contact_name = "+919413512895"
    # Get the message to send
    speak("what i should i send sir ")
    message = listen().lower()

    # Get the current time

    # Send the message
    kit.sendwhatmsg_instantly(f"{contact_name}", f"{message}", wait_time=10, tab_close=True)

    # speak(f"Messege sent successfully")


def Send_massege_on_Whatsapp2():
    # Get the name of the contact

    # speak("who do you want to massege sir")
    contact_name = "papa"

    if contact_name == "papa":
        contact_name = "+918226098666"

    elif contact_name == "girlfriend":
        contact_name = "+919413512895"
    # Get the message to send
    # speak("what i should i send sir ")
    message = "GOOD NIGHT PAPA JI OR MUMMY JI ! JAY SHREE RAM ! RADHEY RADHEY !"
    # Get the current time

    # Send the message
    kit.sendwhatmsg_instantly(f"{contact_name}", f"{message}", wait_time=8, tab_close=True)

    speak(f"Messege sent successfully")


def Send_massege_on_Whatsapp3():
    # Get the name of the contact

    # speak("who do you want to massege sir")
    contact_name = "girlfriend"

    if contact_name == "papa":
        contact_name = "+918226098666"

    elif contact_name == "girlfriend":
        contact_name = "+919413512895"
    # Get the message to send
    # speak("what i should i send sir "
    responses = ["GOOD NIGHT ! SLEEP WELL ! TAKE CARE ! RADHEY RADHEY !", "Good night ,Sweet dreams ! RADHEY RADHEY !",
                 "good night ! RADHEY RADHEY ! TAKE CARE ! SLEEP WELL",
                 "GOOD NIGHT ! RADHEY RADHEY ! i will meet you new dream world"]
    response = random.choice(responses)

    message = response
    # Get the current time

    # Send the message
    kit.sendwhatmsg_instantly(f"{contact_name}", f"{message}", wait_time=8, tab_close=True)

    speak(f"Messege sent successfully")