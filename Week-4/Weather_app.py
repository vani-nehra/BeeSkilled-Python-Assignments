import requests

API_KEY = "c7e3054a785a71643cce5e5f904eadae"

city = input("Enter city name: ")

url = "https://api.openweathermap.org/data/2.5/weather"

params = {
    "q": city,
    "appid": API_KEY,
    "units": "metric"
}

try:
    response = requests.get(url, params=params)

    data = response.json()

    if response.status_code == 200:

        print("\n===== WEATHER INFORMATION =====")
        print("City:", data["name"])
        print("Temperature:", data["main"]["temp"], "°C")
        print("Feels Like:", data["main"]["feels_like"], "°C")
        print("Humidity:", data["main"]["humidity"], "%")
        print("Weather:", data["weather"][0]["description"])
        print("Wind Speed:", data["wind"]["speed"], "m/s")

    else:
        print("\nSomething went wrong!")
        print("Error:", data.get("message", "Unknown error"))

except requests.exceptions.RequestException as e:
    print("Connection error:", e)