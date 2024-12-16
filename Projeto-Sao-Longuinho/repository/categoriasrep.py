from longDAO import CATEGORIASdao
from models import Categorias
from database import db

class CategoriasRepository:

    def __init__(self) -> None:
        self.CATEGORIASdao = CATEGORIASdao()

    def get_categoria(self, id):
        return self.CATEGORIASdao.get_categoria(id)
    
    def get_categorias(self):
        return self.CATEGORIASdao.get_categorias()

    def add_categoria(self, name):
        return self.CATEGORIASdao.add_categoria(name)
    
    def mod_categoria(self, id, name):
        return self.CATEGORIASdao.mod_categoria(id, name)
    
    def delete_categoria(self, id):
        return self.CATEGORIASdao.add_categoria(id)