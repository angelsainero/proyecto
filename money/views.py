import requests
from flask import render_template
from . import app
from .models import DBManager


RUTA = "data/money.db"


@app.route("/")
def inicio():
    db = DBManager(RUTA)
    movimientos = db.consultaSQL("SELECT * from movimientos")
    return render_template("inicio.html", movs=movimientos)


@app.route("/purchase", methods=["GET", "POST"])
def purchase():
    return render_template("purchase.html")


@app.route("/status",  methods=["GET"])
def status():
    return render_template("status.html")
