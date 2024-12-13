from flask import Blueprint, Response, render_template, redirect, url_for, request, session, flash, abort, make_response
from models import *
from database import db, init_db

funcionarios = Blueprint('func',__name__)

@funcionarios.route('/painel/worker')
def painel_worker():
    return render_template('painel_w.html')

@funcionarios.route('/sua-equipe')
def equipe():
    return render_template('equipe.html')

@funcionarios.route('/pendentes')
def pendentes():
    return render_template('pendentes.html')

@funcionarios.route('/achados')
def achados():
    return render_template('equipe.html')

@funcionarios.route('/objeto/<int:id>')
def objeto():
    return render_template('objeto.html')

@funcionarios.route('/perfil/worker', methods=['GET', 'POST'])
def perfil():
    if request.method == 'POST':
        return render_template('edit_perfil_w.html')
    else:
        return render_template('perfil_w.html')