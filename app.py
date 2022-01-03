# importaciones de metodos para web scraping
#import webscraaping

# librerias para la creacion de la api
from flask import Flask
from flask_cors import CORS
# imports routers -------------------------------
from routers.genericrout import genericrouters
#################################################
import ssl
# *********************************Api***************************************

# inicialisando la plataforma de flast
app = Flask(__name__, template_folder='plantillas')
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})

# configuracio de cors


@app.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers',
                         'Content-Type,Authorization')
    response.headers.add('Access-Control-Allow-Methods',
                         'GET,PUT,POST,DELETE,OPTIONS')
    return response

# peticion generica principal


@app.route('/', methods=["GET", "POST"])
def messeg():
    return {"messege": "la aplicacion esta funcionando muy bien"}


# routeres --------------------------------------------
app.register_blueprint(genericrouters)

if __name__ == '__main__':
    app.run()
