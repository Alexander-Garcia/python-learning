# the actual challenge uses Twilio and Python Anywhere but I didn't feel like doing that
# Standard lib imports first
# related 3rd party second
# local last
import os
import requests
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv('API_KEY')
LAT = 48.208176
LONG = 16.373819
WEATHER_URL = "https://api.openweathermap.org/data/2.5/forecast"

parameters = {
    "lat": LAT,
    "lon": LONG,
    "appid": api_key,
}

def is_rain_forecast(weather_ids_list):
    for id in weather_ids_list:
        return "Rain" if id < 700 else "All groovy"

response = requests.get(url=WEATHER_URL, params=parameters)
response.raise_for_status()
data = response.json()
weather_list = [weather["weather"] for weather in data["list"]]
# real descriptive right here
weather_id_list = [weather["id"] for w in weather_list for weather in w]

print(is_rain_forecast(weather_id_list))
