import requests
import argparse

def get_weather(city, units='metric'):
    geocoding_url = f"https://api.open-meteo.com/v1/search?name={city}"
    response = requests.get(geocoding_url)
    location = response.json()['results'][0]
    latitude = location['latitude']
    longitude = location['longitude']
    unit_param = 'metric' if units == 'metric' else 'imperial'
    weather_url = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&hourly=temperature_2m,weathercode&timezone=auto"
    weather_response = requests.get(weather_url)
    current_weather = weather_response.json()['current_weather']
    hourly_forecast = weather_response.json()['hourly']
    return current_weather, hourly_forecast

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Get weather information for a city.')
    parser.add_argument('city', type=str, help='City name to get weather for')
    parser.add_argument('--units', choices=['metric', 'imperial'], default='metric', help='Units for temperature')
    args = parser.parse_args()
    weather, forecast = get_weather(args.city, args.units)
    print(weather)
    print(forecast)
