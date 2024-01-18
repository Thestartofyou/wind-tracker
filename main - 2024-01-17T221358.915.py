import requests
import json

def get_weather(api_key, city):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        'q': city,
        'appid': api_key
    }

    response = requests.get(base_url, params=params)
    data = response.json()

    if response.status_code == 200:
        return data
    else:
        print(f"Error: {data['message']}")
        return None

def track_wind(api_key, city):
    weather_data = get_weather(api_key, city)

    if weather_data:
        wind_speed = weather_data['wind']['speed']
        wind_direction = weather_data['wind']['deg']

        print(f"Wind Speed: {wind_speed} m/s")
        print(f"Wind Direction: {wind_direction} degrees")

# Replace 'YOUR_API_KEY' with your actual OpenWeatherMap API key
api_key = 'YOUR_API_KEY'
city_to_track = 'YourCity,YourCountry'  # Replace with the city you want to track

track_wind(api_key, city_to_track)
