import requests

def get_weather(city):
    geocoding_url = f"https://api.open-meteo.com/v1/search?name={city}"
    response = requests.get(geocoding_url)
    location = response.json()['results'][0]
    latitude = location['latitude']
    longitude = location['longitude']
    weather_url = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&daily=temperature_2m_max,temperature_2m_min,precipitation_probability_max,weathercode&timezone=auto"
    weather_response = requests.get(weather_url)
    current_weather = weather_response.json()['current_weather']
    wmo_code = current_weather['weathercode']
    description = get_weather_description(wmo_code)
    forecast = weather_response.json()['daily']
    daily_forecast = [
        {
            'date': forecast['time'][i],
            'high': forecast['temperature_2m_max'][i],
            'low': forecast['temperature_2m_min'][i],
            'precipitation': forecast['precipitation_probability_max'][i],
            'condition': get_weather_description(forecast['weathercode'][i])
        }
        for i in range(len(forecast['time']))
    ]
    return current_weather, description, daily_forecast


def get_weather_description(wmo_code):
    descriptions = {
        0: "Clear sky",
        1: "Mainly clear",
        2: "Partly cloudy",
        3: "Overcast",
        45: "Fog",
        48: "Deposit of fog",
        61: "Rain showers",
        63: "Rain",
        80: "Rain showers",
        95: "Thunderstorm"
    }
    return descriptions.get(wmo_code, "Unknown weather")