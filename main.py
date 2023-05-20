#Por: Mateo Misas
#Visita: https://mateomisas.simple.ink/

import json
import requests

def obtener_info_clima():
    # Realizar una solicitud GET a una API de OpenWeatherMap
    API_KEY = '508f2197d4bad999c0791cdc2bc11625'
    ciudad = input('Ingresa el nombre de la ciudad: ')

    url = f'https://api.openweathermap.org/data/2.5/weather?q={ciudad}&units=metric&appid={API_KEY}'

    response = requests.get(url)


    # Verificar el código de respuesta
    if response.status_code == 200:
        # Si no hay problemas, se almacena la response en la variable data
        data = response.json()
        temp = data['main']['temp']
        desc = data['weather'][0]['description']
        print(f'Temperatura: {temp} C°')
        print(f'Descripción: {desc}')
    else:
        print('Error al llamar a la API. Código de estado:', response.status_code)

if __name__ == '__main__':
    obtener_info_clima()