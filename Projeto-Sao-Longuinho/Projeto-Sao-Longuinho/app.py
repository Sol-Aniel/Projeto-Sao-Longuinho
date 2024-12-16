from flask import Flask,jsonify, render_template, session, redirect, url_for, request, flash, abort
from flask_sqlalchemy import SQLAlchemy
from database import db, init_db
from controllers import *
from repository import *
import logging

app = Flask(__name__)

app.secret_key = 'longuinho'

app.register_blueprint(clientes)
app.register_blueprint(funcionarios)
app.register_blueprint(administradores)
app.register_blueprint(geral)

app.config['SESSION_COOKIE_SECURE'] = True
app.config['SESSION_COOKIE_HTTPONLY'] = True
logging.basicConfig(level=logging.ERROR, filename='error.log', filemode='a')
logging.getLogger().addHandler(logging.StreamHandler())

@app.errorhandler(404)
def paginaNaoEncontrada(e):
    return render_template('404.html'), 404

@app.errorhandler(Exception)
def handle_generic_error(e):
    return render_template('generic.html', message=str(e)), 500

if __name__ == "__main__":
    init_db(app)
    app.run()