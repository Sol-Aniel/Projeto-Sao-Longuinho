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
    precos = []
    for p in pedidos:
        if p.price:
            precos.append(p.price)
    valor = sum(precos)
    return render_template('pedidos.html', pedidos=pedidos, valor=valor)

@clientes.route('/pedidos/excluir/<int:obj_id>', methods=['POST'])
def excluir_pedidos(obj_id):
    obj = objetos_rep.get_objeto(obj_id)
    if not obj.team_id:
        sucesso = objetos_rep.delete_objeto(obj_id)
        if sucesso == True:
            flash("Objeto excluído com sucesso", "success")
            name_ = session.get('name')
            resp = make_response(redirect(url_for('cliente.pedidos')))
            c_name = "DELETE {}".format(name_)
            c_value = "PEDIDO {} EXCLUÍDO".format(obj.title)
            resp.set_cookie(c_name, c_value)
            session['cookies'].append(f"{c_name}: {c_value}")
            return resp
        else:
            flash(sucesso, "danger")
            return redirect(url_for('cliente.pedidos'))
    else: 
        flash("Uma equipe já foi designada, impossível excluir objeto", "danger")
        return redirect(url_for('geral.objeto', obj_id=obj_id))

@clientes.route('/solicitar', methods=['GET', 'POST'])
def solicitar():
    if request.method == 'POST':
        title = request.form['titulo']
        photo = request.files['foto'].read()
        client_id = session.get('id')
        category_id = request.form['category_id']
        description = request.form['descricao']
        team_id = None
        found = False
        plural = bool(request.form.get('plural', None))
        size = float(request.form['tamanho'])
        weight = float(request.form['peso'])
        lost_local = request.form['lost_local']
        lost_date = request.form['lost_date']
        lost_date = datetime.strptime(lost_date, '%Y-%m-%d').date()
        comments = request.form['comentarios']
        price = None

        sucesso = objetos_rep.add_objeto(title, photo, client_id, category_id, description, team_id, found, plural, size, weight, lost_local, lost_date, comments, price)
        if sucesso == True:  
            flash('Objeto adicionado! Aguarde aprovação de busca', 'sucess')
            name_ = session.get('name')
            resp = make_response(redirect(url_for('cliente.painel')))
            c_name = "ADD {}".format(name_)
            c_value = "PEDIDO {} ADIONADO".format(title)
            resp.set_cookie(c_name, c_value)
            session['cookies'].append(f"{c_name}: {c_value}")
            return resp
        else: 
            flash(sucesso, "danger")
            categorias = categorias_rep.get_categorias()
            return render_template('solicitar.html', categorias=categorias)
    else:
        categorias = categorias_rep.get_categorias()
        return render_template('solicitar.html', categorias=categorias)
    
@clientes.route('/perfil')
def perfil():
    id = session.get('id')
    cliente = clientes_rep.get_cliente(id)
    return render_template('perfil.html', cliente = cliente)

@clientes.route('/edit/perfil', methods=['GET', 'POST'])
def edit_perfil():
    client_id = session.get('id')
    cliente = clientes_rep.get_cliente(client_id)
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
                name_ = session.get('name')
                resp = make_response(redirect(url_for('cliente.painel')))
                c_name = "EDIT {}".format(name_)
                c_value = "PERFIL {} EDITADOO".format(nome)
                resp.set_cookie(c_name, c_value)
                session['cookies'].append(f"{c_name}: {c_value}")
                return resp
            else:
                flash(sucesso, "danger")
                return render_template('editar_perfil.html', cliente = cliente)
        else:
            flash(mensagem, 'danger')
            return render_template('editar_perfil.html', cliente = cliente)
    else:
        return render_template('editar_perfil.html', cliente = cliente)
