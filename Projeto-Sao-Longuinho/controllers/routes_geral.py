from flask import Blueprint, Response, render_template, redirect, url_for, request, session, flash, abort, make_response
from models import *
from repository import *
from database import db, init_db

geral = Blueprint('geral',__name__)

@geral.route('/')
def index():
    return render_template('index.html')

@geral.route('/sobre')
def sobre():
    return render_template('sobre.html')

@geral.route('/login', methods=['GET', 'POST'])
def login():
        if request.method == 'POST':
            email = request.form['email']
            senha = request.form['password']
            acess = validarUser(email, senha)
            if acess == 'admin':
                flash('Login efetuado', 'success')
                session['acess'] = acess
                return redirect(url_for('admin.dashboard'))
            elif acess == 'cliente':
                flash('Login efetuado', 'success')
                session['acess'] = acess
                return redirect(url_for('cliente.painel'))
            elif acess == 'func':
                flash('Login efetuado', 'success')
                session['acess'] = acess
                return redirect(url_for('func.painel_worker'))
            else:
                flash('Usuário não encontrado ou senha incorreta', 'danger')
                return render_template("login.html")
        else:
            return render_template('login.html')

@geral.route('/cadastro', methods=['GET', 'POST'])
def cadastro():
    if request.method == 'POST':
        nome = request.form['nome']
        email = request.form['email']
        telefone = request.form['telefone']
        nacionalidade = request.form['nacionalidade']
        endereco = request.form['endereco']
        senha = request.form['senha']
        flash('Cliente cadastrado', 'success')
        clientes_rep.add_cliente(nome, email, telefone, nacionalidade, endereco, senha)
        return redirect(url_for('geral.index'))
    else:   
        return render_template('cadastro.html')

@geral.route('/objeto/<int:id>')
def objeto():
    if session:
        return render_template('objeto.html')
    else:
        return abort(403)

@geral.route('/logout', methods=['GET', 'POST'])
def logout():
    if session:
        if request.method == 'POST':
            session.clear()
            return redirect(url_for('geral.login'))
        else:
            return render_template('logout.html')
    else:
        return redirect(url_for('geral.index'))