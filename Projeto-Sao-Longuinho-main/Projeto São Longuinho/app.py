from flask import Flask,jsonify, render_template, redirect, url_for, request, flash, abort
from flask_sqlalchemy import SQLAlchemy
from database import db, init_db
from models import Livros
from controllers import *

app = Flask(__name__)
init_db(app)
app.secret_key = 'longuinho'

app.register_blueprint(clientes)
app.register_blueprint(funcionarios)
app.register_blueprint(administradores)

if __name__ == "__main__":
    app.run()
