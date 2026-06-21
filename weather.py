# This script fetches current weather data for a city
# and prints it out

import requests

# Replace YOUR_API_KEY_HERE with your real API key from openweathermap.org
from dotenv import load_dotenv
import os

load_dotenv()
API_KEY = os.getenv("WEATHER_API_KEY")
CITY = "New York"

url = f"https://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}&units=metric"

response = requests.get(url)
data = response.json()

city_name = data["name"]
temperature = data["main"]["temp"]
feels_like = data["main"]["feels_like"]
humidity = data["main"]["humidity"]
description = data["weather"][0]["description"]

print(f"Weather in {city_name}:")
print(f"Temperature: {temperature}°C (feels like {feels_like}°C)")
print(f"Condition: {description}")
print(f"Humidity: {humidity}%")
import csv
from datetime import datetime

# Save this reading to a CSV file
with open("weather_log.csv", "a", newline="") as file:
    writer = csv.writer(file)
    writer.writerow([datetime.now(), city_name, temperature, feels_like, humidity, description])

print("Saved to weather_log.csv")