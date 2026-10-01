from flask import Flask, render_template

main = Flask(__name__)

@main.route("/")
def inicio():
    return render_template("inicio.html")

@main.route("/hola")
def hola():
    return "<h1>Hola mundo</h1>"

@main.route("/enter")
def inter():
    return render_template("intermedio.html", variable1 = "Este es intermedio.")

@main.route("/final")
def Final():
    return render_template("final.html", variable1 = "Este es el final.")

@main.route("/eventos")
def eventos():
    listaEventos = [{
        "Nombre":"Benjita",
        "Fecha" : "Hoy",
        "Lugar" : "Bolivia",
        "Invitados":"Muchos",
        "Precio": 20.5
    },{
        "Nombre":"Bryan",
        "Fecha" : "Manana",
        "Lugar" : "Peru",
        "Invitados":"Pocos",
        "Precio": 17.5
    },{
        "Nombre":"Gonza",
        "Fecha" : "Ayer",
        "Lugar" : "Chile",
        "Invitados":"Bastante",
        "Precio": 31.8
    }]
    return render_template("eventos.html", eventos = listaEventos)

@main.route("/1fn")
def primfn():
    return render_template("1fn.html")
@main.route("/2fn")
def secfn():
    return render_template("2fn.html")

@main.route("/3fn")
def terfn():
    return render_template("3fn.html")

@main.route("/4fn")
def cuarfn():
    return render_template("4fn.html")

@main.route("/5fn")
def quintfn():
    return render_template("5fn.html")

@main.route("/6fn")
def sixtfn():
    return render_template("6fn.html")