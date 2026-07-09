import requests

def get_weather(city):
    geocoding_url = f"https://api.open-meteo.com/v1/search?name={city}"
    response = requests.get(geocoding_url)
    location = response.json()['results'][0]
    latitude = location['latitude']
    longitude = location['longitude']
    weather_url = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current_weather=true"
    weather_response = requests.get(weather_url)
    current_weather = weather_response.json()['current_weather']
    wmo_code = current_weather['weathercode']
    description = get_weather_description(wmo_code)
    return {
        'temperature': current_weather['temperature'],
        'wind_speed': current_weather['windspeed'],
        'description': description
    }


def get_weather_description(wmo_code):
    descriptions = {
        0: "clear sky",
        1: "mainly clear",
        2: "partly cloudy",
        3: "overcast",
        45: "fog",
        48: "fog",
        61: "drizzle",
        63: "rain",
        80: "rain showers",
        95: "thunderstorm",
        99: "thunderstorm with hail"
    }
    return descriptions.get(wmo_code, "unknown")