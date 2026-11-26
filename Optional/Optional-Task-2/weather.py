"""
Current weather for a place name (Optional Task 2).

Asks for a place name, finds its coordinates, and shows the current weather
there. Uses the Open-Meteo geocoding and forecast APIs, which need no API key.

Run it in the terminal with:  python3 weather.py
The web page in server.py uses the same lookup.

Uses only the Python standard library, so no packages need installing.
"""

import json
import urllib.error
import urllib.parse
import urllib.request

GEOCODING_URL = "https://geocoding-api.open-meteo.com/v1/search"
FORECAST_URL = "https://api.open-meteo.com/v1/forecast"
TIMEOUT_SECONDS = 10

# Open-Meteo reports conditions as WMO weather codes. This maps them to text.
WEATHER_CODES = {
    0: "Clear sky",
    1: "Mainly clear",
    2: "Partly cloudy",
    3: "Overcast",
    45: "Fog",
    48: "Depositing rime fog",
    51: "Light drizzle",
    53: "Moderate drizzle",
    55: "Dense drizzle",
    56: "Light freezing drizzle",
    57: "Dense freezing drizzle",
    61: "Slight rain",
    63: "Moderate rain",
    65: "Heavy rain",
    66: "Light freezing rain",
    67: "Heavy freezing rain",
    71: "Slight snow",
    73: "Moderate snow",
    75: "Heavy snow",
    77: "Snow grains",
    80: "Slight rain showers",
    81: "Moderate rain showers",
    82: "Violent rain showers",
    85: "Slight snow showers",
    86: "Heavy snow showers",
    95: "Thunderstorm",
    96: "Thunderstorm with slight hail",
    99: "Thunderstorm with heavy hail",
}


class WeatherError(Exception):
    """Raised when a place can't be found or the weather data is unusable."""


def get_json(url, params):
    """Call an Open-Meteo URL with the given parameters and return the JSON."""
    query = urllib.parse.urlencode(params)
    with urllib.request.urlopen(f"{url}?{query}", timeout=TIMEOUT_SECONDS) as response:
        return json.load(response)


def find_location(place):
    """Return the first geocoding match for a place name.

    Open-Meteo leaves out the "results" key when nothing matches.
    """
    data = get_json(GEOCODING_URL, {"name": place, "count": 1, "format": "json"})
    results = data.get("results")
    if not results:
        raise WeatherError(f"No location found for '{place}'.")
    return results[0]


def get_current_weather(latitude, longitude):
    """Return (current conditions, units) for a set of coordinates."""
    data = get_json(
        FORECAST_URL,
        {
            "latitude": latitude,
            "longitude": longitude,
            "current": "temperature_2m,relative_humidity_2m,wind_speed_10m,weather_code",
            "timezone": "auto",
        },
    )
    return data["current"], data["current_units"]


def describe_place(location):
    """Build a readable name such as 'London, England, United Kingdom'."""
    parts = [location.get("name"), location.get("admin1"), location.get("country")]
    unique = []
    for part in parts:
        if part and part not in unique:
            unique.append(part)
    return ", ".join(unique)


def describe_weather_code(code):
    """Return the text for a WMO weather code."""
    return WEATHER_CODES.get(code, f"Unknown (code {code})")


def get_weather_for_place(place):
    """Look up a place and return its current weather as a dictionary.

    Raises WeatherError if the place isn't found. Network errors (OSError)
    and unexpected responses (KeyError, ValueError) are left for the caller.
    """
    location = find_location(place)
    latitude = location["latitude"]
    longitude = location["longitude"]
    current, units = get_current_weather(latitude, longitude)
    return {
        "place": describe_place(location),
        "latitude": latitude,
        "longitude": longitude,
        "time": current["time"],
        "temperature": current["temperature_2m"],
        "temperature_unit": units["temperature_2m"],
        "humidity": current["relative_humidity_2m"],
        "humidity_unit": units["relative_humidity_2m"],
        "wind_speed": current["wind_speed_10m"],
        "wind_speed_unit": units["wind_speed_10m"],
        "conditions": describe_weather_code(current["weather_code"]),
    }


def display_weather(weather):
    """Print the weather dictionary in the terminal."""
    print(f"Weather for {weather['place']}")
    print(f"Time        : {weather['time']}")
    print(f"Temperature : {weather['temperature']} {weather['temperature_unit']}")
    print(f"Humidity    : {weather['humidity']} {weather['humidity_unit']}")
    print(f"Wind speed  : {weather['wind_speed']} {weather['wind_speed_unit']}")
    print(f"Conditions  : {weather['conditions']}")


def main():
    """Ask for a place name and show its current weather."""
    place = input("Enter a place name: ").strip()
    if not place:
        print("A place name is required.")
        return

    try:
        weather = get_weather_for_place(place)
    except WeatherError as error:
        print(error)
        return
    except OSError as error:
        # URLError and timeouts are both OSError subclasses.
        print(f"Unable to reach Open-Meteo: {error}")
        return
    except (KeyError, ValueError):
        print("Open-Meteo returned data in an unexpected format.")
        return

    display_weather(weather)


if __name__ == "__main__":
    main()
