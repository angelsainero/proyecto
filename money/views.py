
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
        return render_template("purchase.html", form=formulario)
    else:
        moneda1 = request.form['moneda1']
        moneda2 = request.form['moneda2']
        cripto = CriptoModel(moneda1, moneda2)
        consultar = cripto.consultar_cambio()
        total = cripto.cambio
        return render_template("purchase.html", numero=total)


@app.route("/status",  methods=["GET"])
def status():
    return render_template("status.html")
