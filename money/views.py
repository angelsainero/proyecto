
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
        formulario = movform(data=request.form)

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
            if formulario.validate():
                return render_template("purchase.html", formulario=formulario, numero=total, calculo=calculo)
            else:
                return render_template("purchase.html", formulario=formulario, numero=total, calculo=calculo, errores=["Ha fallado la validacion de los datos"])

        elif formulario.enviar.data:
            if formulario.validate():
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
                resultado = db.consultaconparametros(consulta, params)
                if resultado:
                    flash("Movimiento actualizado correctamente",
                          category="exito")
                    return redirect(url_for("inicio"))
                return render_template("purchase.html", formulario=formulario, numero=total, calculo=calculo, errores=["Ha fallado la operación de guardar en la base de datos"])
            else:
                return render_template("purchase.html", formulario=formulario, numero=total, calculo=calculo, errores=["Ha fallado la validacion de los datos"])
        else:
            return render_template("purchase.html", formulario=formulario, numero=total, calculo=calculo)


@app.route("/status",  methods=["GET"])
def status():
    db = DBManager(RUTA)
    euro_to = db.consultaresultado(
        "SELECT sum(cantidad_to) FROM movimientos WHERE moneda_to='EUR'")
    euro_to = euro_to[0]
    euro_from = db.consultaresultado(
        "SELECT sum(cantidad_from) FROM movimientos WHERE moneda_from='EUR'")
    euro_from = euro_from[0]
    saldo_euros_invertidos = euro_to-euro_from
    saldo_euros_invertidos = round(saldo_euros_invertidos, 8)
    total_euros_ivertidos = euro_from
    # total monedas from convertidas a EUROS
    valorcryptofrom = db.consultaresultado_totales(
        "SELECT moneda_from, sum(cantidad_from) FROM movimientos GROUP BY moneda_from")

    totales_from = []
    for valor_from in valorcryptofrom:
        cripto = CriptoModel(valor_from[0], "EUR")
        resultado = cripto.consultar_cambio()
        resultado = cripto.cambio
        resultado = float(resultado)
        resultado = resultado*valor_from[1]
        resultado = totales_from.append(resultado)
    sumavalorfrom = sum(totales_from)

# total monedas to convertidas a euros
    valorcryptoto = db.consultaresultado_totales(
        "SELECT moneda_to, sum(cantidad_to) FROM movimientos GROUP BY moneda_to")

    totales_to = []
    for valor_to in valorcryptoto:
        cripto = CriptoModel(valor_to[0], "EUR")
        resultado = cripto.consultar_cambio()
        resultado = cripto.cambio
        resultado = float(resultado)
        resultado = resultado*valor_to[1]
        resultado = totales_to.append(resultado)
    sumavalorto = sum(totales_to)

    atrapada = sumavalorto-sumavalorfrom
    valoractual = total_euros_ivertidos+saldo_euros_invertidos+atrapada
    valoractual = round(valoractual, 8)

    return render_template("status.html", euro_to=euro_to, euro_from=euro_from, saldo_euros_invertidos=saldo_euros_invertidos, valoractual=valoractual)
