import requests
from config import Config

def get_weather(city):

    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={Config.WEATHER_API_KEY}&units=metric"

    response = requests.get(url)
    data = response.json()

    weather = {
        "temperature": data["main"]["temp"],
        "humidity": data["main"]["humidity"],
        "wind_speed": data["wind"]["speed"],
        "description": data["weather"][0]["description"]
    }

    return weather