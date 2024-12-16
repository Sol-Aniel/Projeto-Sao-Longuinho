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
    func = func_rep.get_func_by('email', email)
    cliente = clientes_rep.get_cliente_by('email', email)
    senha_hash = admin.password_hash
    if admin and admin_rep.check_password(senha, senha_hash):
        return 'admin'
    elif func and func_rep.check_password(senha, senha_hash):
        return 'func'
    elif cliente and clientes_rep.check_password(senha, senha_hash):
        return 'cliente'
    else: 
        return False