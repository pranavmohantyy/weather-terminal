# Weather Terminal

A simple terminal weather app using the Open-Meteo API.

## Features
- No API key required
- Fetches current weather data based on city name

## Usage
1. Run the script with a city name:
   ```bash
   python weather.py "City Name"
   ```
2. Optionally specify units (metric or imperial):
   ```bash
   python weather.py "City Name" --units imperial
   ```

## Example
```bash
python weather.py "Los Angeles"
```

This will return the current weather conditions for Los Angeles.