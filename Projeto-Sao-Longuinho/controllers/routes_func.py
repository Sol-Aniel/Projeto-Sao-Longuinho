from flask import Blueprint, Response, render_template, redirect, url_for, request, session, flash, abort, make_response
from models import *
from database import db, init_db
from repository import *

funcionarios = Blueprint('func',__name__)

@funcionarios.before_request
def verifica():
    if session.get('acess') != 'func':
        return abort(403)

@funcionarios.route('/painel/worker')
def painel_worker():
    return render_template('painel_w.html')

@funcionarios.route('/sua-equipe')
def equipe():
    funcionario_id = session.get('id')  
    funcionario = func_rep.get_funcionario(funcionario_id)
    equipe_id = funcionario.team_id
    equipe = equipes_rep.get_equipe(equipe_id)
    return render_template('equipe.html', equipe=equipe)

@funcionarios.route('/pendentes')
def pendentes():
    objetos_pendentes = objetos_rep.get_objetos_by('found', False)
    return render_template('pendentes.html', objetos=objetos_pendentes)

@funcionarios.route('/achados')
def achados():
    objetos_achados = objetos_rep.get_objetos_by('found', True)
    return render_template('achados.html', objetos=objetos_achados)

@funcionarios.route('/alterar-status/<int:obj_id>', methods=['POST'])
def modstatus(obj_id):
    sucesso = objetos_rep.update_found(obj_id, True)
    if sucesso == True:
        flash("Ojeto dado como achado.", "success")
        return redirect(url_for('func.achados'))
    else:
        flash(sucesso, "danger")
        return redirect(url_for('func.pendentes'))

@funcionarios.route('/perfil/worker', methods=['GET', 'POST'])
def perfil():
    if request.method == 'POST':
        name = request.form['nome']
        team_id = request.form['team_id']
        type_id = request.form['type_id']
        email = request.form['email']
        phone = request.form['telefone']
        salary = request.form['salario']
        adress = request.form['endereco']
        senha = request.form['senha']
        id = session.get('id')
        validade, mensagem = validarSenha(senha)
        if validade == True:
            sucesso = func_rep.mod_funcionario(id, name, team_id, type_id, email, phone, salary, adress, senha)
            if sucesso == True:
                flash('Seu perfil foi atualizado!', 'sucess')
                return redirect(url_for('func.painel_worker'))
            else:
                flash(sucesso, "danger")
                return render_template('perfil_w.html')
        else:
            flash(mensagem, 'danger')
            return render_template('perfil_w.html')
    else:
        id = session.get('id')
        func = func_rep.get_funcionario(id)
        name = func.name
        team = equipes_rep.get_equipe(func.team_id)
        team = team.name
        type_ = tiposrep.get_tipo(func.type_id)
        type_ = type_.name
        email = func.email
        phone = func.phone
        salary = func.salary
        adress = func.adress
        password_hash = func.password_hash
        return render_template('perfil_w.html', name=name, team_id=team_id, type_id=type_id, email=email, phone=phone, salary=salary, adress=adress, password_hash=password_hash)
