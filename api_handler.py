import requests
import json

URL = 'https://api.tequila.kiwi.com/v2/search'

# Definir los encabezados de la solicitud
headers = {
    'apikey': 'aTmwwtK4gL_OG4UJ_5Mv7xVn7lnCkR_0'
}

data = {
    "fly_from": 'FRA',
    "date_from": '2024-04-01',
    "date_to": '2024-04-02',
}

# Realizar la solicitud GET a la API de Tequila
response = requests.get(url=URL, params=data, headers=headers)

# Verificar si la solicitud fue exitosa (código de estado 200)
if response.status_code == 200:
   # Convertir la respuesta descomprimida de JSON a un diccionario de Python
    data = json.loads(response.content)

    # Procesar los datos según sea necesario
    print(data)
else:
    print("La solicitud no fue exitosa. Código de estado:", response.status_code)
    print(response.json())
