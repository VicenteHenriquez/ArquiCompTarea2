import requests


def handle(req):
    url = "http://api.openweathermap.org/data/2.5/weather?q=Santiago&appid=02f431d0b81013512efe09a7de94b50e&units=metric"
    #url para obtener el clima de Santiago
    payload={}
    headers = {}

    response = requests.request("GET", url, headers=headers, data=payload)

    ciudad = response.json()['name']
    temperatura1 = response.json()['main']
    temperatura = temperatura1['temp']
    tempmax = temperatura1['temp_max']

    #print(f"La temperatura de {ciudad} es de {temperatura} grados")

    url1 = "http://api.cmfchile.cl/api-sbifv3/recursos_api/uf?apikey=8554a65077f9b0080a615964cb3865abb6baa5d1&formato=json"
    #url para obtener el valor de la UF
    payload1={}
    headers1 = {}

    response1 = requests.request("GET", url1, headers=headers1, data=payload1)
    valoruf = response1.json()['UFs']
    valoruf1 = valoruf[0]['Valor']

    #print(f"El valor de la UF actualmente es de {valoruf1} CLP")

    url3 = "http://api.cmfchile.cl/api-sbifv3/recursos_api/dolar?apikey=8554a65077f9b0080a615964cb3865abb6baa5d1&formato=json"
    #url para obtener el valor del dolar
    payload3={}
    headers3 = {}

    response3 = requests.request("GET", url3, headers=headers3, data=payload3)
    valordolar = response3.json()['Dolares']
    valordolar1 = valordolar[0]['Valor']

    #print(f"El valor del dolar actualmente es de {valordolar1} CLP")
    urlcruc = "https://elpais.com/juegos/crucigramas/experto/"

    return """<!DOCTYPE html>
    <h2><center>Los datos actualmente son: </center></h2>
    <h3><center>La temperatura en {ciudad} es {temperatura} grados centígrados y una máxima de {tempmax} grados centígrados</center></h3>
    <h3><center>El valor de la UF actualmente es de {valoruf} CLP</center></h3>
    <h3><center>El valor del Dolar a día de hoy es de {valordolar} CLP</center></h3>
    <h3><a href={urlcruc} target= "_blank"><center>{urlcruc}</center></a></h3>
    </html>""".format(ciudad=ciudad, temperatura=temperatura, valoruf=valoruf1, valordolar=valordolar1, urlcruc=urlcruc, tempmax=tempmax)