import requests
import json

# Tu nombre de usuario de GeoNames
api_key = 'EduardoLeon12c'

# Paso 1: Obtener el código del país usando las coordenadas
params_code = {
    'lat': '47.0',
    'lng': '10.2',
    'username': api_key
}
response_code = requests.get('http://api.geonames.org/countryCodeJSON', params=params_code)

if response_code.status_code == 200:
    data_code = response_code.json()
    country_code = data_code['countryCode']
    print(f"Código del país: {country_code}")

    # Paso 2: Usar el código para obtener el nombre del país
    params_info = {
        'country': country_code,
        'username': api_key
    }
    response_info = requests.get('http://api.geonames.org/countryInfoJSON', params=params_info)

    if response_info.status_code == 200:
        data_info = response_info.json()
        country_name = data_info['geonames'][0]['countryName']
        print(f"Nombre del país: {country_name}")
    else:
        print(f"Error al obtener el nombre del país. Código de estado: {response_info.status_code}")
else:
    print(f"Error al obtener el código del país. Código de estado: {response_code.status_code}")
