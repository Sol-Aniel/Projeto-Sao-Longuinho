from flask import Blueprint,render_template

longuinho = Blueprint('longuinho',__name__)

@longuinho.route('/')
def index():
    return f"Longuinho"
