"""
Travel Weather Tool

Shows weather and country information for any city.

Usage:
    python day3i_travel_info.py

Requirements:
    pip install requests python-dotenv
    OPENWEATHER_API_KEY in .env file
"""

import requests
import os
import json
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("OPENWEATHER_API_KEY")

def get_weather(city):
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    return None

def get_country_info(country_code):
    url = f"https://restcountries.com/v3.1/alpha/{country_code}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        if isinstance(data, list) and len(data) > 0:
            return data[0]
        if isinstance(data, dict) and "population" in data:
            return data
    return None

def save_to_file(data, filename):
    with open(filename, "w") as f:
        json.dump(data, f, indent=2)
    print(f"Data saved to {filename}")

def run_tool():
    print("Travel Weather Tool")
    print("-------------------")
    print("Type 'quit' to exit")

    while True:
        city = input("\nEnter a city name: ").strip()

        if city.lower() == "quit":
            print("Thanks for using Travel Tool! Bye 👋")
            break

        if not city:
            print("No city entered. Try again.")
            continue

        print(f"\nFetching data for {city}...")

        weather_data = get_weather(city)

        if not weather_data:
            print(f"Could not find weather data for '{city}'. Check the city name and try again.")
            continue

        # SAVE hapa - hii ndio mpya!
        save_to_file(weather_data, f"{city.lower()}_weather.json")

        main = weather_data.get("main", {})
        weather_list = weather_data.get("weather", [{}])
        wind = weather_data.get("wind", {})
        sys_info = weather_data.get("sys", {})

        country_code = sys_info.get("country", "Unknown")
        country_data = get_country_info(country_code) if country_code != "Unknown" else None

        print(f"\n=== {city.title()}, {country_code} ===")
        print(f"Temperature : {main.get('temp', 'N/A')}C")
        print(f"Condition   : {weather_list[0].get('description', 'N/A').title()}")
        print(f"Humidity    : {main.get('humidity', 'N/A')}%")
        print(f"Wind        : {wind.get('speed', 'N/A')} m/s")

        if country_data:
            population = country_data.get("population", 0)
            region = country_data.get("region", "Unknown")
            currencies = ", ".join(country_data.get("currencies", {}).keys())
            print(f"\n=== Country Info ===")
            print(f"Region      : {region}")
            print(f"Population  : {population:,}")
            print(f"Currency    : {currencies}")
        else:
            print("\nCountry info not available.")

run_tool()