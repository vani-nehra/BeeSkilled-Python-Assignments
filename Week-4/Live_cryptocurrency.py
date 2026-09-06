# crypto_price.py

import requests


coin = input("Enter cryptocurrency name (example: bitcoin): ").lower()

url = "https://api.coingecko.com/api/v3/simple/price"

params = {
    "ids": coin,
    "vs_currencies": "usd,inr"
}


try:

    response = requests.get(url, params=params)

    data = response.json()

    if coin in data:

        print("\n===== CRYPTOCURRENCY PRICE =====")

        print("Cryptocurrency:", coin.capitalize())
        print("Price in USD: $", data[coin]["usd"])
        print("Price in INR: ₹", data[coin]["inr"])

    else:

        print("Cryptocurrency not found.")


except requests.exceptions.RequestException:

    print("Unable to connect to the API.")