# app/commands/weather.py

import requests

def get_weather(location):
    api_key = "your_api_key"  # Replace with your actual API key
    base_url = f"http://api.openweathermap.org/data/2.5/weather?q={location}&appid={api_key}&units=metric"
    response = requests.get(base_url)
    data = response.json()
    
    if data["cod"] != "404":
        weather_description = data["weather"][0]["description"]
        temperature = data["main"]["temp"]
        return f"The weather in {location} is currently {weather_description} with a temperature of {temperature}°C."
    else:
        return f"Sorry, I couldn't find weather information for {location}."
