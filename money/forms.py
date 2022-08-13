from datetime import date, datetime
from flask_wtf import FlaskForm
from wtforms import HiddenField, DateField, StringField, SelectField, SubmitField, TimeField, IntegerField
from wtforms.validators import DataRequired


class movform(FlaskForm):

    fecha = DateField("Fecha")
    hora = TimeField("Hora")
    moneda1 = SelectField("From: ", choices=[(
        "EUR", "EUR"), ("ETH", "ETH"), ("BNB", "BNB"), ("BTC", "BTC")], validators=[DataRequired(message="Debes seleccionar moneda inicial")])
    moneda2 = SelectField("To: ", choices=[(
        "EUR", "EUR"), ("ETH", "ETH"), ("BNB", "BNB"), ("BTC", "BTC")], validators=[DataRequired(message="Debes seleccionar moneda final")])
    cantidad = IntegerField("Cantidad", validators=[
                            DataRequired(message="Debes indicar una cantidad")])
    consultarapi = SubmitField("ConsultarAPI")
    borrar = SubmitField("Borrar")
    enviar = SubmitField("Guardar")
