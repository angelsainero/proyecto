
from time import time
from flask import render_template, request, redirect, flash, url_for
from . import app
from .models import DBManager
from .models import CriptoModel
from .forms import movform
from datetime import date, datetime


RUTA = "data/money.db"


@app.route("/")
def inicio():
    db = DBManager(RUTA)
    movimientos = db.consultaSQL("SELECT * from movimientos")
    return render_template("inicio.html", movs=movimientos)


@app.route("/purchase", methods=["POST", "GET"])
def purchase():

    if request.method == "GET":
        formulario = movform()
        return render_template("purchase.html", formulario=formulario)
    else:
        formulario = movform()

        moneda1 = formulario.moneda1.data
        moneda2 = formulario.moneda2.data
        cantidad = formulario.cantidad.data

        cripto = CriptoModel(moneda1, moneda2)
        consultar = cripto.consultar_cambio()
        total = cripto.cambio
        total = float(round(total, 10))

        cantidad = float(round(cantidad, 10))
        calculo = cripto.cambio
        calculo = float(round(calculo, 10))
        total = total*cantidad
        if formulario.consultarapi.data:

            return render_template("purchase.html", formulario=formulario, numero=total, calculo=calculo)

        elif formulario.enviar.data:

            formulario = movform(data=request.form)
            db = DBManager(RUTA)
            consulta = "INSERT INTO movimientos (date, time, moneda_from, cantidad_from, moneda_to, cantidad_to) VALUES(?,?,?,?,?,?)"
            cantidad = float(formulario.cantidad.data)
            moneda1 = str(formulario.moneda1.data)
            moneda2 = str(formulario.moneda2.data)
            formulario.fecha.data = date.today()
            fecha = formulario.fecha.data
            formulario.hora.data = datetime.today().strftime("%H:%M:%S")
            hora = formulario.hora.data
            params = (fecha, hora, moneda1, cantidad, moneda2, total)
            db.consultaconparametros(consulta, params)


@app.route("/status",  methods=["GET"])
def status():
    return render_template("status.html")
