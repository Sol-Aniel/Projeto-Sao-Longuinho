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
    funcionarios = func_rep.get_funcionarios()
    tipos = tipos_rep.get_tipos()
    objetos = objetos_rep.get_objetos()
    return render_template('equipes.html', objetos=objetos, tipos=tipos, equipes=equipes, funcionarios=funcionarios)

@administradores.route('/equipe/add/', methods=['GET', 'POST'])
def add_equipes():
    if request.method == 'POST':
        name = request.form["nome"]
        funcs_id = request.form.getlist('funcionarios[]')
        equipe_nova = []
        for f in funcs_id:
            func = func_rep.get_funcionario(f)
            equipe_nova.append(func)
        sucesso = equipes_rep.add_equipe(name)
        if sucesso == True:
            flash("Equipe Adicionada com sucesso!", "sucess")
            for func in equipe_nova:
                equipe = equipes_rep.get_equipes_by('name', name)
                equipe_id = equipe[0].id
                func_rep.update_equipe(func.id, equipe_id)
            name_ = session.get('name')
            resp = make_response(redirect(url_for('admin.equipes')))
            c_name = "ADD {}".format(name_)
            c_value = "EQUIPE {} ADIONADA".format(name)
            resp.set_cookie(c_name, c_value)
            session['cookies'].append(f"{c_name}: {c_value}")
            return resp
        else:
            flash(sucesso, "danger")
            return redirect(url_for('admin.add_equipes'))
    else:
        funcionarios = func_rep.get_funcionarios_by('team_id', None)
        tipos = tipos_rep.get_tipos()
        return render_template('add_equipe.html', tipos=tipos, funcionarios=funcionarios)

@administradores.route('/equipes/edit/<int:equipe_id>', methods=['GET', 'POST'])
def edit_equipes(equipe_id):
    equipe = equipes_rep.get_equipe(equipe_id)
    funcs_equipe = func_rep.get_funcionarios_by('team_id', equipe_id)
    funcs = func_rep.get_funcionarios_by('team_id', None)
    tipos = tipos_rep.get_tipos()
    if request.method == 'POST':
        nome = request.form['nome']
        funcs_id = request.form.getlist('funcionarios_id[]')
        equipe_nova = []
        for f in funcs_id:
            func = func_rep.get_funcionario(f)
            equipe_nova.append(func)
        funcs = func_rep.get_funcionarios()
        sucesso = equipes_rep.mod_equipe(equipe_id, nome)
        if sucesso == True:
            flash("Equipe Atualizada com sucesso", "sucess")
            for func in funcs:
                if func.team_id == equipe_id and func not in equipe_nova:
                    func_rep.update_equipe(func.id, None)
            for func in equipe_nova:
                func_rep.update_equipe(func.id, equipe_id)
            name_ = session.get('name')
            resp = make_response(redirect(url_for('admin.dashboard')))
            c_name = "EDIT {}".format(name_)
            c_value = "EQUIPE {} EDITADA".format(nome)
            resp.set_cookie(c_name, c_value)
            session['cookies'].append(f"{c_name}: {c_value}")
            return resp
        else:
            flash(sucesso, "danger")
            return render_template('edit_equipe.html', equipe=equipe, funcionarios=funcs, funcs_equipe=funcs_equipe, tipos=tipos)
    else:
        return render_template('edit_equipe.html', equipe=equipe, funcionarios=funcs, funcs_equipe=funcs_equipe, tipos=tipos)

@administradores.route('/solicitacoes', methods=['GET', 'POST'])
def solicitacoes():
    objetos = objetos_rep.get_objetos_by('team_id', None)
    equipes = equipes_rep.get_equipes()
    clientes = clientes_rep.get_clientes()
    return render_template('solicitacoes.html', clientes=clientes, equipes=equipes, objetos=objetos)

@administradores.route('/aprovar/<int:obj_id>', methods=['POST'])
def aprovar(obj_id):
    price = request.form['preco']
    team_id = request.form['equipe_id']
    sucesso = objetos_rep.approve(obj_id, price, team_id)
    if sucesso == True:
        flash("Objeto Aprovado!", 'sucess')
        name_ = session.get('name')
        resp = make_response(redirect(url_for('admin.solicitacoes')))
        c_name = "APPROVE {}".format(name_)
        obj = objetos_rep.get_objeto(obj_id)
        c_value = "OBJETO {} APROVADO".format(obj.title)
        resp.set_cookie(c_name, c_value)
        session['cookies'].append(f"{c_name}: {c_value}")
        return resp
    else:
        flash(sucesso, 'sucess')
        return redirect(url_for('admin.solicitacoes'))

@administradores.route('/funcionarios')
def funcionarios():
    funcionarios = func_rep.get_funcionarios()
    equipes = equipes_rep.get_equipes()
    tipos = tipos_rep.get_tipos()
    return render_template('funcionarios.html', funcionarios=funcionarios, equipes=equipes, tipos=tipos)

@administradores.route('/funcionarios/add/', methods=['GET', 'POST'])
def add_funcionarios():
    equipes = equipes_rep.get_equipes()
    tipos = tipos_rep.get_tipos()
    if request.method == 'POST':
        nome = request.form['nome']
        equipe_id = request.form['equipe_id']
        tipo_id = request.form['tipo_id']
        email = request.form['email']
        telefone = request.form['telefone']
        salario = request.form['salario']
        endereco = request.form['endereco']
        senha = request.form['senha']
        validade, mensagem = validarSenha(senha)
        if validade == True:
            sucesso = func_rep.add_funcionario(nome, equipe_id, tipo_id, email, telefone, salario , endereco, senha)
            if sucesso == True:
                flash('Funcionario cadastrado', 'success')
                name_ = session.get('name')
                resp = make_response(redirect(url_for('admin.dashboard')))
                c_name = "ADD {}".format(name_)
                c_value = "FUNCIONARIO {} ADICIONADO".format(nome)
                resp.set_cookie(c_name, c_value)
                session['cookies'].append(f"{c_name}: {c_value}")
                return resp
            else:
                flash(sucesso, "danger")
                return render_template('add_funcionario.html', equipes=equipes, tipos=tipos)
        else:
            flash(mensagem, 'danger')
            return render_template('add_funcionario.html', equipes=equipes, tipos=tipos)
    else:
        return render_template('add_funcionario.html', equipes=equipes, tipos=tipos)

@administradores.route('/funcionarios/edit/<int:func_id>', methods=['GET', 'POST'])
def edit_funcionarios(func_id):
    func = func_rep.get_funcionario(func_id)
    equipes = equipes_rep.get_equipes()
    tipos = tipos_rep.get_tipos()
    equipe = equipes_rep.get_equipe(func.team_id)
    tipo = tipos_rep.get_tipo(func.type_id)
    if request.method == 'POST':
        nome = request.form['nome']
        equipe_id = request.form['equipe_id']
        tipo_id = request.form['tipo_id']
        email = request.form['email']
        telefone = request.form['telefone']
        salario = request.form['salario']
        endereco = request.form['endereco']
        senha = request.form['senha']
        validade, mensagem = validarSenha(senha)
        if validade == True:
            sucesso = func_rep.mod_funcionario(func_id, nome, equipe_id, tipo_id, email, telefone, salario , endereco, senha)
            if sucesso == True:
                flash('Funcionario atualizado', 'success')
                name_ = session.get('name')
                resp = make_response(redirect(url_for('admin.dashboard')))
                c_name = "EDIT {}".format(name_)
                c_value = "FUNCIONARIO {} EDITADO".format(nome)
                resp.set_cookie(c_name, c_value)
                session['cookies'].append(f"{c_name}: {c_value}")
                return redirect(url_for('admin.dashboard'))
            else:
                flash(sucesso, "danger")
                return render_template('edit_funcionarios.html', funcionario=func, equipes=equipes, tipos=tipos, equipe=equipe, tipo=tipo)
        else:
            flash(mensagem, 'danger')
            return render_template('edit_funcionarios.html', funcionario=func, equipes=equipes, tipos=tipos, equipe=equipe, tipo=tipo)
    else:
        return render_template('edit_funcionarios.html',funcionario=func, equipes=equipes, tipos=tipos, equipe=equipe, tipo=tipo)

@administradores.route('/add/admin', methods=['GET', 'POST'])
def add_admin():
    if request.method == 'POST':
        nome = request.form['nome']
        email = request.form['email']
        senha = request.form['senha']
        validade, mensagem = validarSenha(senha)
        if validade == True:
            sucesso = admin_rep.add_admin(nome, email, senha)
            if sucesso == True:
                flash('Administrador cadastrado', 'success')
                name_ = session.get('name')
                resp = make_response(redirect(url_for('admin.dashboard')))
                c_name = "ADD {}".format(name_)
                c_value = "ADMINISTRADOR {} ADICIONADO".format(nome)
                resp.set_cookie(c_name, c_value)
                session['cookies'].append(f"{c_name}: {c_value}")
                return resp
            else:
                flash(sucesso, "danger")
                return render_template('add_admin.html')
        else:
            flash(mensagem, 'danger')
            return render_template('add_admin.html')
    else:
        return render_template('add_admin.html')
