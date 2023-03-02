# Vladyslav Davydenko
import requests
from requests.exceptions import HTTPError
import datetime

# Function to convert Kelvin to Celsius
def kel_to_cels(temp):
    return round(temp - 273.15)

# Main Function
def get_weather_forecast():
    # Obtaining responce using OpenWeatherMap
    api_key = "18656a311d81909f9e0e5c54b6fd6995"
    city = "Mustamäe"

    # Error handling
    try:
        request_url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&lat=44.34&lon=10.99&appid={api_key}"
        response = requests.get(request_url)
    except HTTPError as http_err:
            print(f'HTTP error occurred: {http_err}')
    except Exception as err:
            print(f'Other error occurred: {err}')
    else:

        # Check of code responce
        if response.status_code == 200:
            # Obtaining json data and saving into variables
            data = response.json()

            # Variables for every required field
            temp_in_kelvin = data["main"]["temp"]
            temp_in_celsius = kel_to_cels(temp_in_kelvin)

            city = data["name"]
            weather_description = data["weather"][0]["description"]

            wind_speed = data["wind"]["speed"]

            min_temp = data["main"]["temp_min"]
            min_temp_celsius = kel_to_cels(min_temp)
            max_temp = data["main"]["temp_max"]
            max_temp_celsius = kel_to_cels(max_temp)

            date = datetime.date.today()

            # Main Print part
            print("\nWeather forecast")
            print("...........................................\n")
            print(f"Weather description: {weather_description}\n")
            print(f"Temperature: {temp_in_celsius} C\n")
            print(f"City: {city}\n")
            print(f"Today is : {date}\n")
            print(f"Wind speed: {wind_speed} m/s\n")
            print(f"Minimum temperature: {min_temp_celsius} C\n")
            print(f"Maximum temperature: {max_temp_celsius} C\n")
            print("...........................................\n")
        else:
            # Error
            print("[-] Error to retrived the weather")

# Running part
if __name__ == '__main__':
    get_weather_forecast()
