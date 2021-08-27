from .. import controllers

from flask import jsonify

@controllers.route("/")
def home():
    return jsonify({
        "/":"Rota de localização"
    })