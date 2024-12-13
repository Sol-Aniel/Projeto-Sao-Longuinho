from flask import Blueprint,render_template

funcionarios = Blueprint('func',__name__)

@funcionarios.route('/f')
def index():
    return f"Longuinho"
