import requests

api_key = "5e170d9c6a12c12a6c0a746119d73be6"
LAT = -33.868820
LON = 151.209290

parameters = {
    "lat": LAT,
    "lon": LON,
    "appid": api_key,
}

response = requests.get("https://api.openweathermap.org/data/3.0/onecall", params=parameters)
response.raise_for_status()
data = response.json()
print(data)
