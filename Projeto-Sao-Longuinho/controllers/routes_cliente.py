from flask import Blueprint, Response, render_template, redirect, url_for, request, session, flash, abort, make_response
from models import *
from repository import *
from database import db, init_db
from datetime import datetime

clientes = Blueprint('cliente',__name__)

@clientes.before_request
def verifica():
    if session.get('acess') != 'cliente':
        return abort(403)

@clientes.route('/painel')
def painel():
    return render_template('painel.html')

@clientes.route('/pedidos')
def pedidos():
    cliente_id = session.get('id')
    pedidos = objetos_rep.get_objetos_by('client_id', cliente_id)
    return render_template('pedidos.html', pedidos=pedidos)

@clientes.route('/pedidos/excluir/<int:obj_id>', methods=['GET', 'POST'])
def excluir_pedidos(obj_id):
    if request.method == 'POST':
        sucesso = objetos_rep.delete_objeto(obj_id)
        if sucesso == True:
            flash("Objeto excluído com sucesso", "success")
            return redirect(url_for('cliente.pedidos'))
        else:
            flash(sucesso, "danger")
            return redirect(url_for('cliente.pedidos'))
    else:
        return render_template('excluir.html')

@clientes.route('/solicitar', methods=['GET', 'POST'])
def solicitar():
    if request.method == 'POST':
        title = request.form['titulo']
        photo = request.files['foto'].read()
        client_id = session.get['id']
        category_id = request.form['category_id']
        description = request.form['descricao']
        team_id = request.form['team_id']
        found = False
        plural = bool(request.form['plural'])
        size = float(request.form['tamanho'])
        weight = float(request.form['peso'])
        lost_local = request.form['lost_local']
        lost_date = request.form['lost_date']
        lost_date = datetime.strptime(lost_date, '%Y-%m-%d').date()
        comments = request.form['comentarios']

        objetos_rep.add_objeto(title, photo, client_id, category_id, description, team_id, found, plural, size, weight, lost_local, lost_date, comments)
        flash('Objeto adicionado! Aguarde aprovação de busca', 'sucess')
    else:
        return render_template('solicitar.html')

@clientes.route('/perfil', methods=['GET', 'POST'])
def perfil():
    if request.method == 'POST':
        nome = request.form['nome']
        email = request.form['email']
        telefone = request.form['telefone']
        nacionalidade = request.form['nacionalidade']
        endereco = request.form['endereco']
        senha = request.form['senha']
        id = session.get('id')
        validade, mensagem = validarSenha(senha)
        if validade == True:
            sucesso = clientes_rep.mod_cliente(id, nome, email, telefone, nacionalidade, endereco, senha)
            if sucesso == True:
                flash('Seu perfil foi atualizado!', 'sucess')
                return redirect(url_for('cliente.painel'))
            else:
                flash(sucesso, "danger")
                return render_template('perfil.html')
        else:
            flash(mensagem, 'danger')
            return render_template('perfil.html')
    else:
        id = session.get('id')
        cliente = clientes_rep.get_cliente(id)
        return render_template('perfil.html', cliente = cliente)