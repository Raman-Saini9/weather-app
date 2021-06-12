import requests
import config

def get_info(city):
	
	base_url =f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={config.KEY}&units=metric'
	data = requests.get(base_url).json()

	city = data['name']
	country = data['sys']['country']
	current_temp = data['main']['temp']
	temp_min = data['main']['temp_min']
	temp_max = data['main']['temp_max']
	decription_before = data['weather'][0]['main']
	description = data['weather'][0]['description']
	wind = data['wind']['speed']
	humidity = data['main']['humidity']

	return city,country,current_temp,temp_max,temp_min,description,decription_before,humidity,wind