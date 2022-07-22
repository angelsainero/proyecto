from . import app


@app.route("/")
def inicio():
    return "página inicio movimientos"


@app.route("/purchase", methods=["GET", "POST"])
def purchase():
    return "página de compra"


@app.route("/status")
def status():
    return "pagina de status"
