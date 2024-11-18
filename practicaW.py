import urllib.request
import urllib.parse
import http.client
import json
def sw(x):
    clima = {
        'Thunderstorm':'Tormenta',
        'Clouds':'Nublado',
        'Clear': 'Despejado',
        'Haze': 'Niebla',
        'Mist':'niebla'
        
    }
    return clima.get(x,x)
try:
    url = "http://api.openweathermap.org/data/2.5/weather?id=3995465&units=metric&APPID=7e008ba385e8b080c96755dc291da837&lang=en"
    f = urllib.request.urlopen(url,timeout=30)
    djson = json.loads(f.read())
    print(djson['coord']['lon'])
    print(sw(djson['weather'][0]['main']))

except:
    print('Error al consultar datos')
 