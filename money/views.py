from flask import render_template

from . import app
from.models import DBManager

RUTA = "data/money.db"


@app.route("/")
def inicio():
    db = DBManager(RUTA)
    movimientos = db.consultaSQL("SELECT * from movimientos")
    return render_template("inicio.html", movs=movimientos)


@app.route("/purchase", methods=["GET", "POST"])
def purchase():
    return "página de compra"


@app.route("/status")
def status():
    return "pagina de status"
