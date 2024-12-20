from longDAO import EQUIPESdao
from models import Equipes
from database import db

class EquipesRepository:

    def __init__(self) -> None:
        self.EQUIPESdao = EQUIPESdao()

    def get_equipe(self, id):
        return self.EQUIPESdao.get_equipe(id)
    
    def get_equipes(self):
        return self.EQUIPESdao.get_equipes()
    
    def get_equipes_by(self, by, value):
        return self.EQUIPESdao.get_equipes_by(by, value)

    def add_equipe(self, name):
        return self.EQUIPESdao.add_equipe(name)
    
    def mod_equipe(self, id, name):
        return self.EQUIPESdao.mod_equipe(id, name)
    
    def delete_equipe(self, id):
        return self.EQUIPESdao.add_equipe(id)