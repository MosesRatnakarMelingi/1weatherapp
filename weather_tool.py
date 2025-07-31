import os
import requests
from dotenv import load_dotenv
from langchain_core.tools import tool # New import for LangChain tool definition

# Load environment variables (ensure this runs if you run this file directly)
load_dotenv()

@tool # This decorator registers the function as a LangChain tool
def get_current_weather(city: str) -> str:
    """
    Fetches the current weather for a specified city using the OpenWeatherMap API.
    Input should be the name of the city (e.g., "London", "New York").
    This tool provides temperature, feels like temperature, description, humidity, and wind speed in Celsius.
    """
    api_key = os.environ.get("OPENWEATHER_API_KEY")
    if not api_key:
        return "Error: OpenWeatherMap API key not found. Please set OPENWEATHER_API_KEY in your .env file."

    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": city,
        "appid": api_key,
        "units": "metric"  # For Celsius. Use "imperial" for Fahrenheit.
    }

    try:
        response = requests.get(base_url, params=params)
        response.raise_for_status()  # Raise an exception for HTTP errors (4xx or 5xx)
        weather_data = response.json()

        if weather_data.get("cod") == 200: # Check if the city was found
            main_data = weather_data["main"]
            weather_description = weather_data["weather"][0]["description"]
            city_name = weather_data["name"]
            country = weather_data["sys"]["country"]

            temperature = main_data["temp"]
            feels_like = main_data["feels_like"]
            humidity = main_data["humidity"]
            wind_speed = weather_data["wind"]["speed"] # in m/s for metric

            result_string = (
                f"Current weather in {city_name}, {country}:\n"
                f"Temperature: {temperature}°C (feels like {feels_like}°C)\n"
                f"Description: {weather_description.capitalize()}\n"
                f"Humidity: {humidity}%\n"
                f"Wind Speed: {wind_speed} m/s"
            )
            return result_string
        else:
            return f"Could not retrieve weather for {city}. Reason: {weather_data.get('message', 'Unknown error.')}"

    except requests.exceptions.HTTPError as http_err:
        if response.status_code == 404:
            return f"City '{city}' not found. Please check the spelling."
        else:
            return f"HTTP error occurred: {http_err} - Status Code: {response.status_code}"
    except requests.exceptions.ConnectionError as conn_err:
        return f"Connection error: Please check your internet connection. {conn_err}"
    except requests.exceptions.Timeout as timeout_err:
        return f"Timeout error: The request took too long to respond. {timeout_err}"
    except requests.exceptions.RequestException as req_err:
        return f"An unexpected error occurred during the API request: {req_err}"
    except Exception as e:
        return f"An unexpected error occurred: {e}"

# Example of how to test this function directly (optional, for verification)
if __name__ == "__main__":
    print("Testing weather tool directly:")
    print(get_current_weather("London"))
    print("-" * 30)
    print(get_current_weather("New York"))
    print("-" * 30)
    print(get_current_weather("NonExistentCity12345")) # Test with a non-existent city