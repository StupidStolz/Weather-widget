from pyowm.owm import OWM
from pyowm.utils.config import get_default_config
config_dict = get_default_config()
config_dict['language'] = 'ru'  # your language here
owm = OWM('2bc4da0ae9b4979d0faaa70a8980655b', config_dict)
place = input("В каком городе/стране: ")
mgr = owm.weather_manager()
observation = mgr.weather_at_place(place)
w = observation.weather
temp = w.temperature('celsius')["temp"]
config_dict = owm.configuration   
print("В городе " + place + " сейчас " + str(w.detailed_status))    
print("Температура сейчас в районе: " + str(temp))

if temp < 8:
    print('Сейчас очень холодно, одевайся тепло!')
elif temp <20:
    print('Сейчас холодно, оденься потеплее.')
else:
	print('Температура норм, одевайся свободно.')