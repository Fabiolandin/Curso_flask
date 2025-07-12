#impor do flask
from flask import Flask, url_for, render_template

#Inicializando Flask
app = Flask(__name__)

#Rotas
@app.route("/")
def ola_mundo():
    titulo = "Gestão de Usuários"
    usuarios = [
        {"nome": "Fabio", "membro_ativo": True},
        {"nome": "Flavia", "membro_ativo": False},
        {"nome": "Angelina", "membro_ativo": True},
    ]
    return render_template("index.html", titulo = titulo, usuarios = usuarios)

#Rotas
@app.route("/sobre")
def pagina_sobre():
    return """
    Testando docstrings
    1, 2, 3, 4, 5, 6, 7, 8, 9
    10!
"""

#Executando Flask
app.run(debug=True)