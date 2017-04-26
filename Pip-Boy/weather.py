#!/usr/bin/env python
# encoding: utf-8

import pyowm
class WeatherForecast():
    
    def __init__(self, cityName):
        self.cityName = cityName
        self.owm = pyowm.OWM('1b0800976558d34e9dfd441c89a6d0e0')  # You MUST provide a valid API key
        self.forecast = self.owm.daily_forecast(self.cityName)
        self.tomorrow = pyowm.timeutils.tomorrow()
        self.forecast.will_be_sunny_at(self.tomorrow)  # Always True in Italy, right? ;-)
        
        # Search for current weather in London (UK)
        observation = self.owm.weather_at_place('London,uk')
        w = observation.get_weather()
        print(w)                      # <Weather - reference time=2013-12-18 09:20,
                                      # status=Clouds>
        
        # Weather details
        w.get_wind()                  # {'speed': 4.6, 'deg': 330}
        w.get_humidity()              # 87
        w.get_temperature('celsius')  # {'temp_max': 10.5, 'temp': 9.7, 'temp_min': 9.0}
        
        # Search current weather observations in the surroundings of
        # lat=22.57W, lon=43.12S (Rio de Janeiro, BR)
        observation_list = self.owm.weather_around_coords(45.78, 12.05)
        
if __name__ == '__main__':
    weather = WeatherForecast('Montebelluna')
    print(weather.owm.weather_at_place)