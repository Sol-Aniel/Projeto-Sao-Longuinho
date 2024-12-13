from flask import Blueprint, Response, render_template, redirect, url_for, request, session, flash, abort, make_response

clientes = Blueprint('client',__name__)

@clientes.route('/')
def index():
    return render_template('index.html')

@clientes.route('/login', methods=['GET', 'POST'])
def login():
    return render_template('login.html')

@clientes.route('/cadastro', methods=['GET', 'POST'])
def cadastro():
    return render_template('cadastro.html')

@clientes.route('/painel')
def painel():
    return render_template('painel.html')

@clientes.route('/pedidos', methods=['GET', 'POST'])
def pedidos():
    return render_template('pedido.html')

@clientes.route('/solicitar', methods=['GET', 'POST'])
def solicitar():
    return render_template('solicitar.html')

@clientes.route('/perfil', methods=['GET', 'POST'])
def perfil():
    if request.method == 'POST':
        return render_template('edit_perfil.html')
    else:
        return render_template('perfil.html')
