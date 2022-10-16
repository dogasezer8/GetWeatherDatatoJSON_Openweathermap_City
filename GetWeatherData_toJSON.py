from urllib import response
import requests
import json


def get_weather_data_and_writetojson():
    url = 'http://api.openweathermap.org/data/2.5/weather?q=Ankara,TR&appid=3dd5c82851e0aad5fd6aca255f1170e9'
    response = requests.get(url)
    weather_data = response.json()

    with open('weather_data.json', 'w') as fp:
        json.dump(weather_data, fp, indent=4)
    return weather_data

weather_data = get_weather_data_and_writetojson()
print(weather_data)
