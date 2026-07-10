import requests

def get_weather(city):
    geocoding_url = f"https://api.open-meteo.com/v1/search?name={city}"
    response = requests.get(geocoding_url)
    location = response.json()['results'][0]
    latitude = location['latitude']
    longitude = location['longitude']
    weather_url = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&hourly=temperature_2m,weathercode&timezone=auto"
    weather_response = requests.get(weather_url)
    current_weather = weather_response.json()['current_weather']
    hourly_forecast = weather_response.json()['hourly']
    weather_code = current_weather['weathercode']
    weather_icon = get_weather_icon(weather_code)
    return current_weather, hourly_forecast, weather_icon


def get_weather_icon(code):
    icons = {
        1: "☀️",
        2: "🌤️",
        3: "☁️",
        4: "🌧️",
        5: "🌩️",
        6: "❄️"
    }
    return icons.get(code, "❓")
