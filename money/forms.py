from datetime import datetime
from flask_wtf import FlaskForm
from wtforms import HiddenField, DateField, StringField, SelectField, DecimalField, SubmitField


class movform(FlaskForm):

    fecha = HiddenField("Fecha")
    hora = HiddenField("Hora")
    moneda1 = SelectField("From: ", choices=[(
        "EUR", "EUR"), ("ETH", "ETH"), ("BNB", "BNB"), ("BTC", "BTC")])
    moneda2 = SelectField("To: ", choices=[(
        "EUR", "EUR"), ("ETH", "ETH"), ("BNB", "BNB"), ("BTC", "BTC")])
    cantidad = DecimalField("Cantidad", places=8)
    consultarapi = SubmitField("ConsultarAPI")
    ratemoneda = DecimalField("Ratemoneda")
    borrar = SubmitField("Borrar")
    enviar = SubmitField("Guardar")
