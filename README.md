# Proyecto Flask-Classic

## Para arrancar la aplicación

1. Generar y activar un entorno virtual
2. Copiar el archivo `.env_template` a `.env` y establecer los valores adecuados
3. Instalar requirements.txt o requirements-dev.txt en funcion de si vas a desarrollar o usar. 
3. Instalar SQLite y crear BBDD
3. Ejecutar la aplicación con `flask run`

## Entorno Virtual 
```shell
python -m venv env

# linux / macos
source ./env/bin/activate
cp .env_template .env

# Windows
.\env\Scripts\activate
copy .env_template .env


flask run
```

## Instalación de requirements
```
pip install -r requirements.txt
````



Recursos
kata 14 mnuto 50 - coinapi
kata 16 1:35:50 - html 
kata 17 02:05:20 - condicionales en el html
kata 18 formularios
kata 19  flask - sql
    bbdd: 1:38:00


https://rest.coinapi.io/v1/exchangerate/{base}/{quota}?time={time}&apikey={apikey}

api_url = f"https: // rest.coinapi.io/v1/exchangerate/{base}/{quota}?time = {time} & apikey = {apikey}
https://rest.coinapi.io/v1/exchanges?apikey=0B9C1C2F-3AC8-4639-9F7B-D2D34D469C67
https://rest.coinapi.io/v1/exchangerate/BTC/USD?apikey=0B9C1C2F-3AC8-4639-9F7B-D2D34D469C67


from coinapi_rest_v1.restapi import CoinAPIv1
import datetime, sys

test_key = sys.argv[1]

api = CoinAPIv1(test_key)
exchanges = api.metadata_list_exchanges()



exchange_rate = api.exchange_rates_get_specific_rate('BTC', 'USD')
print('Rate: %s' % exchange_rate['rate'])