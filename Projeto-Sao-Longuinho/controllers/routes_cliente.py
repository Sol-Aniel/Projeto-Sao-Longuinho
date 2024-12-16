from flask import Blueprint, Response, render_template, redirect, url_for, request, session, flash, abort, make_response
from models import *
from database import db, init_db

clientes = Blueprint('cliente',__name__)

@clientes.before_request
def verifica():
    if session.get('acess') != 'cliente':
        return abort(403)

@clientes.route('/painel')
def painel():
    return render_template('painel.html')

@clientes.route('/pedidos', methods=['GET', 'POST'])
def pedidos():
    return render_template('pedidos.html')

@clientes.route('/pedidos/excluir/<int:id>', methods=['GET', 'POST'])
def excluir_pedidos():
    return render_template('excluir.html')

@clientes.route('/solicitar', methods=['GET', 'POST'])
def solicitar():
    return render_template('solicitar.html')

@clientes.route('/perfil', methods=['GET', 'POST'])
def perfil():
    if request.method == 'POST':
        return render_template('edit_perfil.html')
    else:
        return render_template('perfil.html')