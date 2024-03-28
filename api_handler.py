import requests
import gzip
import json

# Path to the gzip-compressed file
gzip_file = 'compressed_file.gz'

url = 'https://api.tequila.kiwi.com/v2/search?fly_from=FRA&date_from=2024-04-01&date_to=2024-04-07'

# ?apikey=&fly_from=origen&date_from=2024-04-01&date_to=2024-04-07

# Definir los encabezados de la solicitud
headers = {
    'Content-Type': 'application/json',  # Tipo de contenido: JSON
    'apikey': '5wQv3lhDl2qVK6Ub7cDDfOX8eGOzkUPR'          # Tu clave de API
}

# Realizar la solicitud GET a la API de Tequila
response = requests.get(url, headers=headers)

# Verificar si la solicitud fue exitosa (código de estado 200)
if response.status_code == 200:
    # Verificar si la respuesta está codificada en gzip
    if response.headers.get('Content-Encoding') == 'gzip':
        # Descomprimir la respuesta gzip
        compressed_data = response.content
        uncompressed_data = gzip.decompress(compressed_data).decode('utf-8')

        # Convertir la respuesta descomprimida de JSON a un diccionario de Python
        data = json.loads(uncompressed_data)

        # Procesar los datos según sea necesario
        print(data)
    else:
        print("La respuesta no está codificada en gzip.")
else:
    print("La solicitud no fue exitosa. Código de estado:", response.status_code)
