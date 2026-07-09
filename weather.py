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
    return {
        'temperature': current_weather['temperature'],
        'wind_speed': current_weather['windspeed'],
        'weather_code': current_weather['weathercode']
    }

if __name__ == '__main__':
    city = input("Enter city name: ")
    print(get_weather(city))
