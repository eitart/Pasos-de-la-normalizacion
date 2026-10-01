from flask import Flask, render_template

main = Flask(__name__)

@main.route("/")
def inicio():
    return render_template("inicio.html")

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