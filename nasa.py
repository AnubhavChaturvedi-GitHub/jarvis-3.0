import requests
import json
from datetime import date
from speak import speak

def get_nasa_report():
    # Get today's date
    today = date.today()

    # NASA API endpoint
    url = "https://api.nasa.gov/planetary/apod"

    # API key
    api_key = "tQm3v64hWonaigY9Ked0xROFLxqG5hhul0LWWt64"

    # API parameters
    params = {
        "api_key": api_key,
        "date": today.strftime("%Y-%m-%d")
    }

    # Send a GET request to the API
    response = requests.get(url, params=params)

    # Parse the JSON response
    data = json.loads(response.text)

    # Print the report
    print("NASA's report for " + today.strftime("%B %d, %Y") + ":")
    print("Title: " + data["title"])
    print("Explanation: " + data["explanation"])
    print("Image URL: " + data["url"])
    speak("NASA's report for " + today.strftime("%B %d, %Y") + ":")
    speak("Title: " + data["title"])
    speak("Explanation: " + data["explanation"])
    speak("Image URL: " + data["url"])

# Example usage
get_nasa_report()
