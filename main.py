import requests
import os
from twilio.rest import Client

account_sid = "AC1bc31d1a2848dd4fcbe160eb0091be2e"
auth_token = os.environ.get("AUTH_TOKEN")

OMW_endpoint = "https://api.openweathermap.org/data/3.0/onecall"
api_key = os.environ.get("OWM_API_KEY")
LAT = 10.311780
LON = 123.916412

parameters = {
    "lat": LAT,
    "lon": LON,
    "appid": api_key,
    "exclude": "current,minutely,daily"
}

response = requests.get(OMW_endpoint, params=parameters)
response.raise_for_status()
data = response.json()
rain_data = data["hourly"][0]["weather"][0]["id"]
rain_data_slice = data["hourly"][:12]

will_rain = False

for hour_data in rain_data_slice:
    condition_code = hour_data["weather"][0]["id"]
    if condition_code < 700:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
        body="It's going to rain today, remember to bring an umbrella ☔️",
        from_='+12133547621',
        to='+61 406 579 199'
        )
    print(message.status)