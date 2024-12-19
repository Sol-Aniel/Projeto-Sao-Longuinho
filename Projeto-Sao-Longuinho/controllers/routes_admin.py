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
    equipes = equipes_rep.get_equipes()
    funcionarios = func_rep.get_funcionarios
    return render_template('equipes.html', equipes=equipes, funcionarios=funcionarios)

@administradores.route('/equipes/add/<int:id>', methods=['GET', 'POST'])
def add_equipes():
    if request.method == 'POST':
        name = request.form["nome"]
        funcs = request.form.getlist('funcionarios[]')
        sucesso = equipes_rep.add_equipe(name)
        if sucesso == True:
            flash("Equipe Adicionada com sucesso!", "sucess")
            for func in funcs:
                equipe = equipes_rep.get_equipes_by('name', name)
                equipe_id = equipe[0].id
                func_rep.update_equipe(func.id, equipe_id)
            return redirect(url_for('admin.equipes'))
        else:
            flash(sucesso, "danger")
            return redirect(url_for('admin.add_equipes'))
    else:
        funcs = func_rep.get_funcionarios_by('team_id', None)
        lideres = []
        funcionarios = funcs
        for func in funcs:
            if func.type_id == 1:
                lideres.append(func)
                funcionarios.remove(func)
        tipos = tipos_rep.get_tipos
        return render_template('add_equipes.html', lideres=lideres, tipos=tipos, funcionarios=funcionarios)

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