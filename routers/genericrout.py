from flask import Blueprint

# inicializamos el blueprint
genericrouters = Blueprint('genericrouters', __name__)


@genericrouters.route("/router/generic/")
def fuctiongeneric():
    return {"messege": "mensaje generico"}
