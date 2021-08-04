import os

import requests
from twilio.rest import Client

response = requests.get(url="https://api.openweathermap.org/data/2.5/onecall?lat=22.565571&lon=88.370209&exclude"
                            "=current,minutely,daily&appid=74d2bf2a063afaa0bddfb06f37ae46af")
response.raise_for_status()

weather_data = response.json()

account_sid = "Your twillio accnt_sid"
auth_token = "acoount_token"

will_rain = False

for i in range(0, 12):
    condition_code = weather_data["hourly"][i]["weather"][0]["id"]
    if int(condition_code) < 600:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)

    message = client.messages \
        .create(
        body="Well,It's About To Rain",
        from_='+twillio num',
        to =''your_num
    )
    print(message.status)
