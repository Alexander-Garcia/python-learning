# The final piece of this is to send myself an email but I'm not putting credentials in here so yeah. 
# TODO: maybe see how python handles env type variables and put email stuff in there?
import requests
from datetime import datetime

# constants
# taken while in Vienna, Austria
LAT = 48.208176
LONG = 16.373819


parameters = {
    "lat": LAT,
    "lng": LONG,
    "formatted": 0,
}


def get_iss_position():
    r = requests.get("http://api.open-notify.org/iss-now.json")
    r.raise_for_status()
    data = r.json()
    return {
        "lat": float(data["iss_position"]["latitude"]),
        "long": float(data["iss_position"]["longitude"])
    }

def get_sunset_sunrise():
    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise_hour = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset_hour = int(data["results"]["sunset"].split("T")[1].split(":")[0])
    return {
        "sunrise_hour": sunrise_hour,
        "sunset_hour": sunset_hour,
    }

local_hours = get_sunset_sunrise()
iss_position = get_iss_position()
current_hour = datetime.now().hour
