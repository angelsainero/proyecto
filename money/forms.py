from datetime import datetime
from flask_wtf import FlaskForm
from wtforms import HiddenField, DateField, StringField, SelectField, DecimalField, SubmitField


class movform(FlaskForm):
    id = HiddenField()
    fecha = HiddenField("Fecha")
    moneda1 = SelectField("From: ", choices=[(
        "EUR", "EUR"), ("ETH", "ETH"), ("BNB", "BNB"), ("BTC", "BTC")])
    moneda2 = SelectField("To: ", choices=[(
        "EUR", "EUR"), ("ETH", "ETH"), ("BNB", "BNB"), ("BTC", "BTC")])
    cantidad = DecimalField("Cantidad", places=8)
    consultarapi = SubmitField("ConsultarAPI")
    enviar = SubmitField("Guardar")
