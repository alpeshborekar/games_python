import requests

def get_weather_data(api_key, city):
    base_url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'
    
    try:
        response = requests.get(base_url)
        data = response.json()
        
        if data['cod'] == 200:  # 200 for suc
            weather = {
                'temperature': data['main']['temp'],
                'humidity': data['main']['humidity'],
                'wind_speed': data['wind']['speed'],
                'description': data['weather'][0]['description']
            }
            return weather
        else:
            print(f"Error: {data['message']}")
            return None
    except requests.exceptions.RequestException as e:
        print(f"Error fetching weather data: {e}")
        return None

def main():
    api_key = 'd329e0790843f4931fbf115903780e3a'


    city = input("Enter city name: ")
    
    weather_data = get_weather_data(api_key, city)
    
    if weather_data:
        print(f"Weather in {city}:")
        print(f"Temperature: {weather_data['temperature']} °C")
        print(f"Humidity: {weather_data['humidity']} %")
        print(f"Wind: {weather_data['wind_speed']} m/s")
        print(f"Description: {weather_data['description']}")
    else:
        print(f"Could not fetch weather data for {city}")

if __name__ == "__main__":
    main()
