from flask import Flask
import requests

apikey = "0B9C1C2F-3AC8-4639-9F7B-D2D34D469C67"


app = Flask(__name__)
app.config.from_prefixed_env()
