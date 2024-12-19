from .adminrep import AdministradoresRepository
from .categoriasrep import CategoriasRepository
from .clientesrep import ClientesRepository
from .equipesrep import EquipesRepository
from .funcrep import FuncionariosRepository
from .objetosrep import ObjetosRepository
from .tiposrep import TiposRepository

admin_rep = AdministradoresRepository()
categorias_rep = CategoriasRepository()
clientes_rep = ClientesRepository()
equipes_rep = EquipesRepository()
func_rep = FuncionariosRepository()
objetos_rep = ObjetosRepository()
tipos_rep = TiposRepository()

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