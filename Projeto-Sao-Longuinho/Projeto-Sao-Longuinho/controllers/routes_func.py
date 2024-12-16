from flask import Blueprint, Response, render_template, redirect, url_for, request, session, flash, abort, make_response
from models import *
from database import db, init_db
from repository import funcrep, objetosrep, equipesrep, tiposrep

funcionarios = Blueprint('func',__name__)
funcrep = funcrep()
objetosrep = objetosrep()
equipesrep = equipesrep()
tiposrep = tiposrep()


@funcionarios.before_request
def verifica():
    if session.get('acess') != 'func':
        return abort(403)
    
# armazenando dados na sessão
def sessionfunc(funcionario):
    session['id'] = funcionario.id
    session['name'] = funcionario.name
    session['acess'] = 'func'

@funcionarios.route('/painel/worker')
def painel_worker():
    return render_template('painel_w.html')

@funcionarios.route('/sua-equipe')
def equipe():
    # caso haja tentativa de acesso nao autenticado pela rota
    funcionario_id = session.get('id')  
    if not funcionario_id:
        flash("Usuário não está logado.", "error")
        return redirect(url_for('func.painel_worker'))
     
    funcionario = Funcionarios.query.get(funcionario_id)
    equipe = funcionario.equipes  
    return render_template('equipe.html', equipe=equipe)


@funcionarios.route('/pendentes')
def pendentes():
    objetos_pendentes = objetosrep.get_objetos_by_status('pendente')
    return render_template('pendentes.html', objetos=objetos_pendentes)

@funcionarios.route('/achados')
def achados():
    objetos_achados = objetosrep.get_objetos_by_status('achado')
    return render_template('achados.html', objetos=objetos_achados)

@funcionarios.route('/alterar-status/<int:id>', methods=['POST'])
def modstatus(id):
    sucesso = objetosrep.update_status(id, 'achado')
    if sucesso:
        flash("Ojeto dado como achado.", "success")
        return render_template('achados.html', sucesso=sucesso)
    else:
        flash("Não foi possível atualizar o status do objeto", "error")
    return redirect(url_for('func.pendentes'))

@funcionarios.route('/perfil/worker', methods=['GET', 'POST'])
def perfil():
    if request.method == 'POST':
        name = request.form['name']
        team_id = request.form['team_id']
        type_id = request.form['type_id']
        email = request.form['email']
        phone = request.form['phone']
        salary = request.form['salary']
        adress = request.form['adress']
        password_hash = request.form['password_hash']
       
        funcrep.mod_funcionario(id, name, team_id, type_id, email, phone, salary, adress, password_hash)
        mensagem = 'Seu perfil foi atualizado!'
        return redirect(url_for('func.painel_worker', mensagem=mensagem))
    else:
        name = funcrep.get_func_by_id(id)
        team_id = equipesrep.get_equipe(funcionarios.id)
        team_id = funcionarios.team_id
        type_id = tiposrep.get_tipo(funcionarios.id)
        type_id = funcionarios.type_id
        email = email.name
        phone = phone.name
        salary = salary.name
        adress = adress.name
        password_hash = password_hash.name
        return render_template('editar.html', id=id, name=name, team_id=team_id, type_id=type_id, email=email, phone=phone, salary=salary, adress=adress, password_hash=password_hash)