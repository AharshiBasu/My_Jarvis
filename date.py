import requests
from datetime import datetime
import pyttsx3


engine = pyttsx3.init()
def speak(text):
    engine.say(text)
    engine.runAndWait()


# Your location
# latitude = 22.67
# longitude = 88.35

# getting location

response = requests.get("https://ipinfo.io/json")
data = response.json()

latitude, longitude = map(float, data["loc"].split(","))

# Get current weather
url = (
    f"https://api.open-meteo.com/v1/forecast?"
    f"latitude={latitude}&longitude={longitude}"
    f"&current=temperature_2m,relative_humidity_2m,weather_code,wind_speed_10m"
)

response = requests.get(url)
data = response.json()

current = data["current"]

# Date and time
now = datetime.now()

speak(f"Date       : {now.strftime("%m-%d-%Y")}")
speak(f"Time       : {now.strftime("%I:%M:%S %p")}")
speak(f"Temperature: {current["temperature_2m"], "°C"}")
speak(f"Humidity   : {current["relative_humidity_2m"], "%"}")
speak(f"Wind Speed : {current["wind_speed_10m"], "kilometer per hour"}")
