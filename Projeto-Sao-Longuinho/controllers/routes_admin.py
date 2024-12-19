from flask import Blueprint, Response, render_template, redirect, url_for, request, session, flash, abort, make_response
from models import *
from repository import *
from database import db, init_db

administradores = Blueprint('admin',__name__)

@administradores.before_request
def verifica():
    if session.get('acess') != 'admin':
        return abort(403)

@administradores.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

@administradores.route('/equipes')
def equipes():
    return render_template('equipes.html')

@administradores.route('/equipes/add/<int:id>', methods=['GET', 'POST'])
def add_equipes():
    return render_template('add_equipes.html')

@administradores.route('/equipes/edit/<int:id>', methods=['GET', 'POST'])
def edit_equipes():
    return render_template('edit_equipes.html')

@administradores.route('/solicitacoes', methods=['GET', 'POST'])
def solicitacoes():
    return render_template('solicitacoes.html')

@administradores.route('/funcionarios')
def funcionarios():
    return render_template('funcionarios.html')

@administradores.route('/funcionarios/add/<int:id>', methods=['GET', 'POST'])
def add_funcionarios():
    return render_template('add_funcionarios.html')

@administradores.route('/funcionarios/edit/<int:id>', methods=['GET', 'POST'])
def edit_funcionarios():
    return render_template('edit_funcionarios.html')

@administradores.route('/add/admin', methods=['GET', 'POST'])
def add_admin():
    if request.method == 'POST':
        return redirect(url_for('admin.dashboard'))
    else:
        return render_template('add_admin.html')