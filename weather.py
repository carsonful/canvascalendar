import requests
import keys
from datetime import date, datetime

def converttemp(x):

	y = 1.8*(x-273) +32
	y = round(y)
	return str(y) + ' °' + 'F'

def convertspeed(x):
    y = x / 1.609344
    y = round(y)
    return y


user_api = keys.weatherapikey
location = keys.weathercity

complete_api_link = "https://api.openweathermap.org/data/2.5/weather?q="+location+"&appid="+user_api
api_link = requests.get(complete_api_link)
api_data = api_link.json()

#create variables to store and display data
temp_city = converttemp(api_data['main']['temp'])
weather_desc = api_data['weather'][0]['description']
hmdt = api_data['main']['humidity']
wind_spd = convertspeed(api_data['wind']['speed'])
date_time = datetime.now().strftime("%d %b %Y | %I:%M:%S %p")


def getweather():

    x = []
    
    x.append(["Weather stats for - " + str(location.upper() + ', ' + date_time)])
    x.append(['Current temperature:',str(temp_city)])
    x.append(['Current weather desc:',str(weather_desc)])
    x.append(['Current Humidity:',str(hmdt) + '%'])
    x.append(['Current wind speed:',str(wind_spd) + 'mph'])

    return x
