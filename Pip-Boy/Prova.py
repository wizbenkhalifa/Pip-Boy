import pyowm

owm = pyowm.OWM('1b0800976558d34e9dfd441c89a6d0e0')  # You MUST provide a valid API key

# Have a pro subscription? Then use:
# owm = pyowm.OWM(API_key='your-API-key', subscription_type='pro')

# Will it be sunny tomorrow at this time in Milan (Italy) ?

# Search for current weather in London (UK)
observation = owm.weather_at_place('Montebelluna,it')
w = observation.get_weather()
# Weather details
w.get_wind()                  # {'speed': 4.6, 'deg': 330}
w.get_humidity()              # 87
w.get_temperature('celsius')  # {'temp_max': 10.5, 'temp': 9.7, 'temp_min': 9.0}
s = str(w).split("status=")
print()
weather = s[s.__len__()-1]
weather = weather.replace(">", "")
temp = str(w.get_temperature('celsius')).split(",")
temperature = temp[0].split(":")[1]
tMax = temp[1].split(":")[1]
tMin = temp[2].split(":")[1]
print(weather," ",temperature,"-",tMax,"-",tMin)