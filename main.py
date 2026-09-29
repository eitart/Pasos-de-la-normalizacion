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
    return render_template("intermedio.html")

@main.route("/final")
def Final():
    return render_template("final.html")

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

