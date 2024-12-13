from flask import Blueprint,render_template

administradores = Blueprint('admin',__name__)

@administradores.route('/a')
def index():
    return f"Longuinho"
