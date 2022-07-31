from flask import Flask
import requests

apikey = "0B9C1C2F-3AC8-4639-9F7B-D2D34D469C67"

cabeceras = {
    "X-CoinAPI-Key": apikey
}

api_url = "https://rest.coinapi.io"
endpoint = "/v1/exchangerate"

url = api_url + endpoint
respuesta = requests.get(url, headers=cabeceras)
if respuesta.status_code == 200:
    print(respuesta.content)


app = Flask(__name__)
