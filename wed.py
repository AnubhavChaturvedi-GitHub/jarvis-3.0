import requests
from bs4 import BeautifulSoup
from speak import speak

def get_weather(location):
    # Construct the URL for the weather website
    url = f'https://weather.com/weather/today/l/{location}'

    # Send an HTTP request to the website
    response = requests.get(url)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the HTML content of the page
        soup = BeautifulSoup(response.text, 'html.parser')

        # Find the element that contains the temperature information
        temperature_element = soup.find('span', {'data-testid': 'TemperatureValue'})

        # Extract the temperature text and remove any non-digit characters
        temperature_fahrenheit = ''.join(char for char in temperature_element.text if char.isdigit())

        # Convert temperature to Celsius
        temperature_celsius = (int(temperature_fahrenheit) - 32) * 5 / 9

        return temperature_celsius
    else:
        # Print an error message if the request was not successful
        print(f"Error: Unable to fetch weather data. Status code: {response.status_code}")
        return None

def temp_outside():
    # Example: Get the weather for a specific location (replace 'your-location' with the desired location)
    location_code = 'f5720f935015d866abbc8f4d5beefe74b16a77fe84928669d117dd882d7de136'
    temperature = get_weather(location_code)

    if temperature is not None:
        speak(f"The current temperature is {temperature:.2f}°C.")
    else:
        speak("Weather data unavailable.")

