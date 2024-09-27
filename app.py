import requests #libreria de python que permite hacer solicitudes HTTP
from dotenv import load_dotenv
import os

# Cargar las variables del archivo .env
load_dotenv()

# Extraer la API Key
api_key = os.getenv("apikey")

def obtener_clima():
    user_input = input("Ingrese la ciudad: ") 
    print(user_input)

    weather_data = requests.get(
        f"https://api.openweathermap.org/data/2.5/weather?q={user_input}&units=metric&APPID={api_key}&lang=es")

    #haciendo la primera solicitud, la url utilizada es un endpoint 
    #el resultado de la solicitud se guarda en la variable weather_data 
    if weather_data.json()['cod'] == '404':
        print("Ciudad no Encontrada")
    else:
        clima = weather_data.json()['weather'][0]['description']
        temperatura = round(weather_data.json()['main']['temp'])
        datos = {
            "ciudad": user_input,
            "temperatura": temperatura,
            "condicion": clima
        }
        return datos 

if __name__ == "__main__":
    datos = obtener_clima()
    if datos:
        print(f"El Clima en {datos['ciudad']} está: {datos['condicion']}")
        print(f"La temperatura en {datos['ciudad']} es: {datos['temperatura']}ºC")
