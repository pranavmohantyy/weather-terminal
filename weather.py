import requests
import argparse
import json

def get_weather(city, units='metric'):
    geocoding_url = f"https://api.open-meteo.com/v1/search?name={city}"
    response = requests.get(geocoding_url)
    location = response.json()['results'][0]
    latitude = location['latitude']
    longitude = location['longitude']
    unit_param = 'metric' if units == 'metric' else 'imperial'
    weather_url = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&hourly=temperature_2m,weathercode,windspeed_10m&timezone=auto"
    weather_response = requests.get(weather_url)
    weather_data = weather_response.json()
    return weather_data

def main():
    parser = argparse.ArgumentParser(description='Get weather information')
    parser.add_argument('city', type=str, help='City name to get the weather for')
    parser.add_argument('--units', type=str, default='metric', choices=['metric', 'imperial'], help='Units of measurement')
    args = parser.parse_args()
    weather = get_weather(args.city, args.units)
    print(json.dumps(weather, indent=2))

if __name__ == '__main__':
    main()