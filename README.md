# Travel Weather Tool

## Problem it solves
Travellers want to know weather + country info in one place.
Instead of checking 2 websites, this tool asks for a city and
shows weather, region, population and currency together.

## What it does
- Asks user for a city name
- Calls OpenWeather API for weather
- Uses the country code from weather to call REST Countries API
- Combines both results into one clean report
- Saves raw weather response to `<city>_weather.json`
- Type `quit` to exit

## How to run
```bash
pip install requests python-dotenv
python day3ii_travel_info.py