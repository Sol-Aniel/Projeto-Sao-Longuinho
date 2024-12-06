from flask import Flask,jsonify, render_template, redirect, url_for, request, flash, abort
from flask_sqlalchemy import SQLAlchemy
from controllers import *

app = Flask(__name__)
app.secret_key = 'chave_secreta'

app.register_blueprint(longuinho)

if __name__ == "__main__":
    app.run()
