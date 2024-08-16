import requests

API_KEY = 'your_api_key_here'  # Replace with your OpenWeatherMap API key
BASE_URL = 'http://api.openweathermap.org/data/2.5/weather'

def get_weather(city_name):
    """Fetch weather data from OpenWeatherMap."""
    params = {
        'q': city_name,
        'appid': API_KEY,
        'units': 'metric'  # Use 'imperial' for Fahrenheit
    }
    response = requests.get(BASE_URL, params=params)
    data = response.json()

    if data['cod'] != 200:
        return None

    weather = {
        'city': data['name'],
        'temperature': data['main']['temp'],
        'description': data['weather'][0]['description'],
        'humidity': data['main']['humidity'],
        'wind_speed': data['wind']['speed']
    }
    return weather

def display_weather(weather):
    """Display weather data."""
    print(f"City: {weather['city']}")
    print(f"Temperature: {weather['temperature']}°C")
    print(f"Weather: {weather['description']}")
    print(f"Humidity: {weather['humidity']}%")
    print(f"Wind Speed: {weather['wind_speed']} m/s")

def main():
    """Main function to run the application."""
    print("Weather App")
    while True:
        city_name = input("Enter city name (or 'exit' to quit): ")
        if city_name.lower() == 'exit':
            break

        weather = get_weather(city_name)
        if weather:
            display_weather(weather)
        else:
            print("City not found or API request failed. Please try again.")

if __name__ == "__main__":
    main()
