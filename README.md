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
kata 19  flask - sql
    bbdd: 1:38:00