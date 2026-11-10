import requests

# Weather ya Isiolo - lat 0.3556, lon 37.5833
url = "https://api.open-meteo.com/v1/forecast?latitude=0.3556&longitude=37.5833&current=temperature_2m,relative_humidity_2m,apparent_temperature,weather_code,wind_speed_10m&timezone=Africa%2FNairobi"

response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    current = data["current"]

    temp = current["temperature_2m"]
    feels_like = current["apparent_temperature"]
    humidity = current["relative_humidity_2m"]
    wind = current["wind_speed_10m"]

    print("--- ISIOLO WEATHER - LIVE ---")
    print(f"Temperature: {temp}°C")
    print(f"Feels Like: {feels_like}°C")
    print(f"Humidity: {humidity}%")
    print(f"Wind Speed: {wind} km/h")
    print("-----------------------------")
else:
    print("Request failed. Status:", response.status_code)