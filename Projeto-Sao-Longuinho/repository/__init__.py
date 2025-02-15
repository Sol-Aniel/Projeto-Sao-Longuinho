from .adminrep import AdministradoresRepository
from .categoriasrep import CategoriasRepository
from .clientesrep import ClientesRepository
from .equipesrep import EquipesRepository
from .funcrep import FuncionariosRepository
from .objetosrep import ObjetosRepository
from .tiposrep import TiposRepository
from datetime import datetime

admin_rep = AdministradoresRepository()
categorias_rep = CategoriasRepository()
clientes_rep = ClientesRepository()
equipes_rep = EquipesRepository()
func_rep = FuncionariosRepository()
objetos_rep = ObjetosRepository()
tipos_rep = TiposRepository()

def setData ():
    admins = admin_rep.get_admins()
    tipos = tipos_rep.get_tipos()
    cats = categorias_rep.get_categorias()
    funcs = func_rep.get_funcionarios()
    equipes = equipes_rep.get_equipes()
    clientes = clientes_rep.get_clientes()
    objetos = objetos_rep.get_objetos()
    if len(admins) == 0:
        admin_rep.add_admin('Mr. Longuinho', 'long@gmail.com', 'Qw1@@@@@')
    if len(equipes) == 0:
        equipes_rep.add_equipe("Armada Celestial")
        equipes_rep.add_equipe("Santa Ceia")
        equipes_rep.add_equipe("Quadrilha Diabrética")
    if len(funcs) == 0:
        func_rep.add_funcionario('Yahweh', 1, 1, 'god@gmail.com', '777', 7777.77, 'Céu', "G@d77777")
        func_rep.add_funcionario('Arcanjo Miguel', 1, 2, 'miguel@gmail.com', '7777', 7777.77, 'Céu', "Migu@l77777")
        func_rep.add_funcionario('Arcanjo Rafael', 1, 3, 'rafael@gmail.com', '77777', 7777.77, 'Céu', "Rafa@l77777")
        func_rep.add_funcionario('Arcanjo Gabriel', 1, 4, 'gabriel@gmail.com', '777777', 7777.77, 'Céu', "Gabri@l77777")
        func_rep.add_funcionario('Arcanjo Uriel', 1, 5, 'uriel@gmail.com', '7777777', 7777.77, 'Céu', "Uri@l77777")

        func_rep.add_funcionario('Jesus Cristo', 2, 1, 'jesus@gmail.com', '777', 6543.21, 'No meio de nós', "J3sus*****")
        func_rep.add_funcionario('Pedro', 2, 2, 'pedro@gmail.com', '00 00000-0000', 1234.56, 'Roma', "P3dr@77777")
        func_rep.add_funcionario('Tiago Maior', 2, 2, 'tiago_maior@gmail.com', '00 00000-0000', 1234.56, 'Judeia', "T1ag@M77777")
        func_rep.add_funcionario('João', 2, 3, 'joao@gmail.com', '00 00000-0000', 1234.56, 'Éfeso', "Jo@o77777")
        func_rep.add_funcionario('André', 2, 4, 'andre@gmail.com', '00 00000-0000', 1234.56, 'Grécia', "Andr3@77777")
        func_rep.add_funcionario('Felipe', 2, 5, 'felipe@gmail.com', '00 00000-0000', 1234.56, 'Frígia', "F3l!pe77777")
        func_rep.add_funcionario('Bartolomeu', 2, 6, 'bartolomeu@gmail.com', '00 00000-0000', 1234.56, 'Armênia', "B@rto77777")
        func_rep.add_funcionario('Mateus', 2, 1, 'mateus@gmail.com', '00 00000-0000', 1234.56, 'Etiópia', "M@teus77777")
        func_rep.add_funcionario('Tiago Menor', 2, 2, 'tiago_menor@gmail.com', '00 00000-0000', 1234.56, 'Jerusalém', "T1ag0m77777")
        func_rep.add_funcionario('Tomé', 2, 3, 'tome@gmail.com', '00 00000-0000', 1234.56, 'Índia', "T@me77777")
        func_rep.add_funcionario('Simão Zelote', 2, 4, 'simao_zelote@gmail.com', '00 00000-0000', 1234.56, 'Mesopotâmia', "S1ma@Z77777")
        func_rep.add_funcionario('Judas Tadeu', 2, 5, 'judas_tadeu@gmail.com', '00 00000-0000', 1234.56, 'Pérsia', "JudasT@d3u")
        func_rep.add_funcionario('Judas Iscariotes', 2, 6, 'x9@gmail.com', '00 00000-0000', 1234.56, 'Jerusalém', "Beij@noOmbro123")

        func_rep.add_funcionario('Estrela da Manhã', 3, 1, 'lucifer@gmail.com', '666', 6666.66, 'Um dia:O Céu', "@rgulhO666")
        func_rep.add_funcionario('Belzebu', 3, 2, 'belzebu@gmail.com', '6666', 6666.66, 'Lago de Lama', "_Gul@666")
        func_rep.add_funcionario('Asmodeus', 3, 3, 'asmodeus@gmail.com', '66666', 6666.24, 'Vale dos Ventos', "Luxuri@666")
        func_rep.add_funcionario('Leviatã', 3, 4, 'leviata@gmail.com', '666666', 6666.66, 'Inferno', "Invej@666")
        func_rep.add_funcionario('Mammon', 3, 5, 'mammon@gmail.com', '6666666', 66666.99, 'Colina de Rocha', "G@nancia666")
        func_rep.add_funcionario('Baphomet', 3, 6, 'baphomet@gmail.com', '6', 0.06, 'Casa', "Preguiç@666")
        func_rep.add_funcionario('Satã', 3, 2, 'satan@gmail.com', '66666666', 6666.66, 'Rio Estige', "__Ir@666")
    if len(clientes) == 0:
        clientes_rep.add_cliente('Sol', 'sol@gmail.com', '11 96639-5228', 'Brasileira', 'Rua Giuseppe Cadura, 69', 'Qw1@@@@@')
    if len(objetos) == 0:
        caminho_imagem = './GitLonguinho/Projeto-Sao-Longuinho/static/images/buraco_negro.jpeg'
        with open(caminho_imagem, 'rb') as f:
            buraco_negro = f.read()
        lost_date = '0001-01-01'
        lost_date = datetime.strptime(lost_date, '%Y-%m-%d').date()
        objetos_rep.add_objeto('Buraco Negro M87*', buraco_negro, 1, 4, 'Ele ficou tímido', 1, True, False, 0.01, 0.1, 'Centro da Galáxia Messier 87', lost_date, 'Ele não gosta de câmeras !!!', 1000000000000000.00)
    
        caminho_imagem = 'GitLonguinho/Projeto-Sao-Longuinho/static/images/4d.gif'
        with open(caminho_imagem, 'rb') as f:
            d4 = f.read()
        lost_date = '2025-01-01'
        lost_date = datetime.strptime(lost_date, '%Y-%m-%d').date()
        objetos_rep.add_objeto('Tesseract', d4, 1, 3, 'Um objeto interdimencional de grande poder', 2, False, True, 20, 100, 'Asgard', lost_date, 'Um trouxa roubou de mim, cuidado com ele!', 2500000000.99)
    
        caminho_imagem = 'GitLonguinho/Projeto-Sao-Longuinho/static/images/esnupi.jpeg'
        with open(caminho_imagem, 'rb') as f:
            esnupi = f.read()
        lost_date = '2024-12-19'
        lost_date = datetime.strptime(lost_date, '%Y-%m-%d').date()
        objetos_rep.add_objeto('Isabel', esnupi, 1, 7, 'Linteralmente o esnupi veyr', 2, True, False, 167, 49, 'IFSP', lost_date, 'Ela passou mal e não pode apresentar :(', 0.99)
    
        caminho_imagem = 'GitLonguinho/Projeto-Sao-Longuinho/static/images/et_bilu.jpeg'
        with open(caminho_imagem, 'rb') as f:
            et_bilu = f.read()
        lost_date = '2010-10-10'
        lost_date = datetime.strptime(lost_date, '%Y-%m-%d').date()
        objetos_rep.add_objeto('Et Bilu', et_bilu, 1, 5, 'Um et cabeçudo e feio', 3, False, False, 148, 25, 'Rio Branco, Acre', lost_date, 'Do nado esse cara chegou ni mim e falou "busquem comer cimento"', 1502)
    if len(tipos) == 0:
        tipos_rep.add_tipo('Líder')
        tipos_rep.add_tipo('Agente')
        tipos_rep.add_tipo('Pesquisador')
        tipos_rep.add_tipo('Técnico')
        tipos_rep.add_tipo('Arqueólogo')
        tipos_rep.add_tipo('Cozinheiro')
    if len(cats) == 0:
        categorias_rep.add_categoria("Eletrônicos")
        categorias_rep.add_categoria("Roupas")
        categorias_rep.add_categoria("Ferramentas")
        categorias_rep.add_categoria("Imóveis")
        categorias_rep.add_categoria("Armas")
        categorias_rep.add_categoria("Acessórios")
        categorias_rep.add_categoria("Outros")

def validarUser (email, senha):
    admin = admin_rep.get_admin_by('email', email)
    func = func_rep.get_funcionarios_by('email', email)
    cliente = clientes_rep.get_clientes_by('email', email)

    if admin:
        asenha_hash = admin[0].password_hash
    if func:
        fsenha_hash = func[0].password_hash
    if cliente:
        csenha_hash = cliente[0].password_hash
    
    if admin and admin_rep.check_password(senha, asenha_hash):
        return 'admin'
    elif func and func_rep.check_password(senha, fsenha_hash):
        return 'func'
    elif cliente and clientes_rep.check_password(senha, csenha_hash):
        return 'cliente'
    else: 
        return False
    
def validarSenha(senha):
    
    if len(senha) < 8:
        return False, "A senha deve ter pelo menos 8 caracteres."

    if not any(char.isupper() for char in senha):
        return False, "A senha deve conter pelo menos uma letra maiúscula."

    if not any(char.islower() for char in senha):
        return False, "A senha deve conter pelo menos uma letra minúscula."

    if not any(char.isdigit() for char in senha):
        return False, "A senha deve conter pelo menos um número."

    caracteres_especiais = "!@#$%^&*()-_=+[{]}\\|;:'\",<.>/?`~"
    if not any(char in caracteres_especiais for char in senha):
        return False, "A senha deve conter pelo menos um caractere especial."

    return True, "Senha válida."

def sobreEncontrados(client_id):
    objetos = objetos_rep.get_objetos_by('client_id', client_id)
    encontrado = False
    for objeto in objetos:
        if objeto.found:
            encontrado = True
    if encontrado:
        return True, "Você tem objetos encontrados! Espere eles chegarem na sua casa pelos Correios!"
    else:
        return False, "Nenhum objeto encontrado até o momento"
    
def sobreAprovados(client_id):
    objetos = objetos_rep.get_objetos_by('client_id', client_id)
    preco = False
    for objeto in objetos:
        if objeto.team_id:
            preco = True
    if preco:
        return True, "Você tem objetos aprovados! Realize o pagamento para começar a busca!"
    else:
        return False, "Nenhum objeto aprovado até o momento"