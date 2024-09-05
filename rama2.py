
import requests

api_key = '8c9da465d252dbb823453ace018c0c6e'


user_input = input("Ingrese la ciudad: ")
print(user_input)

weather_data = requests.get(
    f"https://api.openweathermap.org/data/2.5/weather?q={user_input}&units=metric&APPID={api_key}")

if weather_data.json()['cod'] == '404':
    print("Ciudad no Encontrada")
else:
    clima = weather_data.json()['weather'][0]['description']
    temperatura = round(weather_data.json()['main']['temp'])

    print(f"El Clima en {user_input} esta: {clima}")
    print(f"La temperatura en {user_input} es: {temperatura}ºC")