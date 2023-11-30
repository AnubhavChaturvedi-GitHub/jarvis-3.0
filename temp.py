import requests
from bs4 import BeautifulSoup
from speak import speak
def Temp():
    search = "temperature in banglore"
    url = f"https://www.google.com/search?q={search}"
    r = requests.get(url)
    data = BeautifulSoup(r.text, "html.parser")
    temperature = data.find("div", class_="BNeawe").text
    print(f"The Temperature Outside Is {temperature}")
    speak(f"The Temperature Outside Is {temperature}")

import requests
import json
from speak import speak

# API endpoint and API key
endpoint = "http://api.openweathermap.org/data/2.5/weather"
api_key = ""

# location
def temcity():
    city = "Satna"

    # send GET request to API endpoint
    response = requests.get(endpoint, params={"q": city, "appid": api_key})

    # parse JSON response
    data = json.loads(response.text)

    # print current temperature
    print("Temperature in " + city + ": " + str(data["main"]["temp"]) + "°F")
    speak("Temperature in " + city + ": " + str(data["main"]["temp"]) + "°F")

temcity()