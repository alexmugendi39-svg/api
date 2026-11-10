import requests

url = "https://restcountries.com/v2/name/kenya"
response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    country = data[0]

    name = country["name"]
    capital = country["capital"]
    population = country["population"]
    currency = country["currencies"][0]["code"]

    print(f"Country: {name}")
    print(f"Capital: {capital}")
    print(f"Population: {population:,}")
    print(f"Currency: {currency}")
else:
    print("Request failed. Status:", response.status_code)