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
    for admin in admin:
        asenha_hash = admin.password_hash
    for func in func:
        fsenha_hash = func.password_hash
    for cliente in cliente:
        csenha_hash = cliente.password_hash
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