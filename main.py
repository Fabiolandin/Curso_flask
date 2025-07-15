#impor do flask
from flask import Flask
from routes.home import home_route

#Inicializando Flask
app = Flask(__name__)

app.register_blueprint(home_route)

#Executando Flask
app.run(debug=True)