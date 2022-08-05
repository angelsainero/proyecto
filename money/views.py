
from flask import render_template, request, redirect, flash, url_for
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
        if formulario.consultarapi.data:
            cripto = CriptoModel("EUR", "BTC")
            consultar = cripto.consultar_cambio()
            total = cripto.cambio
            return render_template("purchase.html", formulario=formulario, numero=total)

        if formulario.enviar.data:
            formulario = movform()
            db = DBManager(RUTA)
            params = (formulario.fecha.data, formulario.hora.data,
                      formulario.moneda1.data, formulario.cantidad.data, formulario.moneda2.data)
            consulta = "INSERT INTO movimientos (date, time, moneda_from, cantidad_from, moneda_to, cantidad_to) VALUES({params})"

            resultado = db.consultaconparametros(consulta, params)
            if resultado:
                flash("Movimiento actualizado correctamente ;)",
                      category="exito")

                return redirect(url_for("inicio"))
            else:
                return "Ha fallado "


@app.route("/status",  methods=["GET"])
def status():
    return render_template("status.html")
