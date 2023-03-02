import requests
from secret import WEATHER_API_KEY

city = 'Put your city name here'
username = "Put your name here"
weather_forecast_url = f'http://api.weatherapi.com/v1/forecast.json?key={WEATHER_API_KEY}&q={city}'
forecast = requests.get(weather_forecast_url).json()


def generate_weather_msg():
    # weather condition
    weather_condition = forecast['forecast']['forecastday'][0]['day']['condition']['text']

    # will it rain?
    rain_prob = forecast['forecast']['forecastday'][0]['day']['daily_chance_of_rain']
    rain_str = ''
    if rain_prob > 50:
        rain_str = 'Bring an umbrella!'
    # the current and forecast temperature
    temperature = forecast['current']['temp_c']
    temp_feels = forecast['current']['feelslike_c']
    max_temp_today = forecast['forecast']['forecastday'][0]['day']['maxtemp_c']
    min_temp_today = forecast['forecast']['forecastday'][0]['day']['mintemp_c']

    # determines the current wind conditions
    wind_condition = ''
    current_wind = forecast['current']['wind_kph']
    if current_wind < 5:
        wind_condition = 'some still air'
    elif (5 < current_wind < 11):
        wind_condition = 'a light breeze'
    elif (11 < current_wind < 19):
        wind_condition = 'a gentle breeze'
    elif (19 < current_wind < 29):
        wind_condition = 'a moderate breeze'
    elif current_wind > 29:
        wind_condition = 'a strong breeze'

    # to be emailed
    message = f'Hi {username}, you are currently in {city}.\nThe weather is: {weather_condition}\nThe temperature today is {temperature}C and it feels like {temp_feels}C.\nThe highest temperature is {max_temp_today}C and the lowest temperature is {min_temp_today}C.\nThere is a {rain_prob}% chance of rain today. {rain_str}\nIn terms of wind, you will be experiencing {wind_condition}.\n'
    return message
