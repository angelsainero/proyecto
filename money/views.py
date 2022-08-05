
from flask import render_template, request
from . import app
from .models import DBManager
from .models import CriptoModel
from .forms import movform


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
        cripto = CriptoModel("EUR", "BTC")
        consultar = cripto.consultar_cambio()
        total = cripto.cambio
        return render_template("purchase.html", formulario=formulario, numero=total)


@app.route("/status",  methods=["GET"])
def status():
    return render_template("status.html")
