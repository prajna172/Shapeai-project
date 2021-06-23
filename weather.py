import requests
#import os
from datetime import datetime

api_key = '87d845b0b6cf29baa1a73cc34b067a95'
location = input("Enter the city name: ")

complete_api_link = "https://api.openweathermap.org/data/2.5/weather?q="+location+"&appid="+api_key
api_link = requests.get(complete_api_link)
api_data = api_link.json()

#create variables to store and display data
temp_city = ((api_data['main']['temp']) - 273.15)
weather_desc = api_data['weather'][0]['description']
hmdt = api_data['main']['humidity']
wind_spd = api_data['wind']['speed']
date_time = datetime.now().strftime("%d %b %Y | %I:%M:%S %p")
 
file = open( 'output.txt' , 'w')

file.write ("-------------------------------------------------------------\n")
file.write ("Weather Stats for - " + location.upper() + " || " + date_time + '\n')
file.write ("-------------------------------------------------------------\n")

file.write ("Current temperature is:" + str(temp_city) + "deg C\n")
file.write ("Current weather desc  :" + weather_desc + '\n')
file.write ("Current Humidity      :" + str(hmdt) + '\n')
file.write ("Current wind speed    :" + str(wind_spd)  + ' kmph\n')
