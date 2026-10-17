from flask import Flask, render_template



app=Flask(__name__)

#un decorador es poniendo un arroba
@app.route("/") #decorador o ruta
def index():
    titulo="Pagina de Inicio"
    listado = ["Python", "Flask", "Jinja", "HTML", "CSS"]
    return render_template("index.html",titulo=titulo,listado=listado)



@app.route("/hola") #decorador o ruta
def hola():
    return "<h1> Hola PWA  - IEVN1003</h1>"

#como pasar parametros por url
@app.route("/user/<string:nom>") #decorador o ruta
def user(nom):
    return "<h1> Hola User:{} </h1> ".format(nom)
    #el format sirve para hacer el preformateo


@app.route("/numero/<int:n>") #decorador o ruta
def numero(n):
    return " Numero: {}".format(n)

@app.route("/user/<int:id>/<string:username>")
def username(id,username):
    return "ID:{} nombre:{}".format(id.username)

@app.route("/suma/<float:n1>/<float:n2>")
def func(n1,n2):
    return "La suma es:{}".format(n1+n2)

if __name__=="__main__":
    app.run(debug=True)