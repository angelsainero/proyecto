from datetime import date, datetime
from flask_wtf import FlaskForm
from wtforms import HiddenField, DateField, StringField, SelectField, DecimalField, SubmitField, TimeField


class movform(FlaskForm):

    fecha = DateField("Fecha")
    hora = TimeField("Hora")
    moneda1 = SelectField("From: ", choices=[(
        "EUR", "EUR"), ("ETH", "ETH"), ("BNB", "BNB"), ("BTC", "BTC")])
    moneda2 = SelectField("To: ", choices=[(
        "EUR", "EUR"), ("ETH", "ETH"), ("BNB", "BNB"), ("BTC", "BTC")])
    cantidad = DecimalField("Cantidad")
    consultarapi = SubmitField("ConsultarAPI")
    borrar = SubmitField("Borrar")
    enviar = SubmitField("Guardar")
