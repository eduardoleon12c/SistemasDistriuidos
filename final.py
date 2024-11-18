import requests
import json

# Tu nombre de usuario de GeoNames y clave de API de OpenWeather
geonames_username = 'EduardoLeon12c'
openweather_api_key = '7e008ba385e8b080c96755dc291da837'

# Paso 1: Obtener el código del país usando las coordenadas
params_code = {
    'lat': '47.0',
    'lng': '10.2',
    'username': geonames_username
}
response_code = requests.get('http://api.geonames.org/countryCodeJSON', params=params_code)

if response_code.status_code == 200:
    data_code = response_code.json()
    country_code = data_code['countryCode']
    print(f"Código del país: {country_code}")

    # Paso 2: Usar el código para obtener el nombre del país y la capital
    params_info = {
        'country': country_code,
        'username': geonames_username
    }
    response_info = requests.get('http://api.geonames.org/countryInfoJSON', params=params_info)

    if response_info.status_code == 200:
        data_info = response_info.json()
        country_name = data_info['geonames'][0]['countryName']
        capital = data_info['geonames'][0]['capital']
        print(f"Nombre del país: {country_name}")
        print(f"Capital del país: {capital}")

        # Paso 3: Obtener el clima en la capital usando OpenWeather
        params_weather = {
            'q': capital,
            'units': 'metric',
            'APPID': openweather_api_key,
            'lang': 'es'  # Idioma español
        }
        response_weather = requests.get('http://api.openweathermap.org/data/2.5/weather', params=params_weather)

        if response_weather.status_code == 200:
            data_weather = response_weather.json()
            # Imprimimos la temperatura y una breve descripción del clima
            temperatura = data_weather['main']['temp']
            descripcion_clima = data_weather['weather'][0]['description']
            print(f"El clima en {capital}, {country_name}:")
            print(f"Temperatura: {temperatura}°C")
            print(f"Descripción: {descripcion_clima.capitalize()}")
        else:
            print(f"Error al obtener el clima. Código de estado: {response_weather.status_code}")
    else:
        print(f"Error al obtener el nombre del país. Código de estado: {response_info.status_code}")
else:
    print(f"Error al obtener el código del país. Código de estado: {response_code.status_code}")
