
import requests
from flask import render_template, request
from . import app
from .models import DBManager
from .models import CriptoModel


RUTA = "data/money.db"


@app.route("/")
def inicio():
    db = DBManager(RUTA)
    movimientos = db.consultaSQL("SELECT * from movimientos")
    return render_template("inicio.html", movs=movimientos)


@app.route("/purchase", methods=["POST", "GET"])
def purchase():
<<<<<<< HEAD
    if request.method == "GET":
        return render_template("purchase.html")
    else:
        moneda1 = request.form['moneda1']
        moneda2 = request.form['moneda2']
        cripto = CriptoModel(moneda1, moneda2)
        consultar = cripto.consultar_cambio()
        total = cripto.cambio
        return render_template("purchase.html", numero=total)
=======
    cripto = CriptoModel("EUR", "BTC")
    consultar = cripto.consultar_cambio()
    total = cripto.cambio
    return render_template("purchase.html", numero=total)
>>>>>>> d68ef624ec3a32988896b49c2113172464998834


@app.route("/status",  methods=["GET"])
def status():
    return render_template("status.html")
