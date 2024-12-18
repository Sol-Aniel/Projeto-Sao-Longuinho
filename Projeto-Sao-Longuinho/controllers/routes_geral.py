from flask import Blueprint, Response, render_template, redirect, url_for, request, session, flash, abort, make_response
from models import *
from repository import *
from database import db, init_db

geral = Blueprint('geral',__name__)

# armazenando dados na sessão
def sessionuser(user):
    for user in user:
        session['id'] = user.id
        session['name'] = user.name

@geral.route('/')
def index():
    return render_template('index.html')

@geral.route('/image/<int:obj_id>')
def get_image(obj_id):
    if session:  
        obj = objetos_rep.get_objeto(obj_id)
        if not obj or not obj.photo:  
            return "Imagem não encontrada", 404
        
        photo = obj.photo
        photo_header = photo[:8]  # Pega os primeiros 8 bytes

        # Verificação dos tipos de imagem baseados nos cabeçalhos
        if photo_header[:2] == b'\xFF\xD8':  # JPEG
            mime_type = 'image/jpeg'
        elif photo_header[:4] == b'\x89\x50\x4E\x47':  # PNG
            mime_type = 'image/png'
        elif photo_header[:6] in (b'GIF87a', b'GIF89a'):  # GIF
            mime_type = 'image/gif'
        else:
            return "Formato de imagem não suportado", 400

        # Retorna a imagem com o MIME type correto
        return Response(photo, mimetype=mime_type)
    else:
        return abort(403)  # Acesso proibido

@geral.route('/sobre')
def sobre():
    return render_template('sobre.html')

@geral.route('/login', methods=['GET', 'POST'])
def login():
        if request.method == 'POST':
            email = request.form['email']
            senha = request.form['senha']
            acess = validarUser(email, senha)
            if acess == 'admin':
                flash('Login efetuado', 'success')
                session['acess'] = acess
                user = admin_rep.get_admin_by('email', email)
                sessionuser(user)
                return redirect(url_for('admin.dashboard'))
            elif acess == 'cliente':
                flash('Login efetuado', 'success')
                session['acess'] = acess
                user = clientes_rep.get_clientes_by('email', email)
                sessionuser(user)
                return redirect(url_for('cliente.painel'))
            elif acess == 'func':
                flash('Login efetuado', 'success')
                session['acess'] = acess
                user = func_rep.get_funcionarios_by('email', email)
                sessionuser(user)
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
        validade, mensagem = validarSenha(senha)
        if validade == True:
            sucesso = clientes_rep.add_cliente(nome, email, telefone, nacionalidade, endereco, senha)
            if sucesso == True:
                flash('Cliente cadastrado', 'success')
                return redirect(url_for('geral.index'))
            else:
                flash(sucesso, "danger")
                return render_template('cadastro.html')
        else:
            flash(mensagem, 'danger')
            return render_template('cadastro.html')
    else:   
        return render_template('cadastro.html')

@geral.route('/objeto/<int:obj_id>')
def objeto(obj_id):
    if session:
        acess = session.get['acess']
        objeto = objetos_rep.get_objeto(obj_id)
        return render_template('objeto.html', acess=acess, objeto=objeto)
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