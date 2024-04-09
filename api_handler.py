import requests

URL = 'https://api.tequila.kiwi.com/v2/search'

# Definir los encabezados de la solicitud
headers = {
    'apikey': 'aTmwwtK4gL_OG4UJ_5Mv7xVn7lnCkR_0'
}

data = {
    "fly_from": "MVD",
    "fly_to": "NYC",
    "date_from": "2024-04-10",
    "date_to": "2025-04-10",
    "return_from": "2024-04-10", #Poner return_form asegura que sea pasaje de ida y vuelta
    "return_from": "2025-04-10",
    "curr": "USD",
}

# Realizar la solicitud GET a la API de Tequila
response = requests.get(url=URL, params=data, headers=headers)
try:
    response.raise_for_status()
except:
    print("La solicitud no fue exitosa. Código de estado:", response.status_code)
    print(response.json())
else:
    data = response.json()
    # Procesar los datos según sea necesario
    print(data)