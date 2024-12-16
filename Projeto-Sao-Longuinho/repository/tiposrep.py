from longDAO import TIPOSdao
from models import Tipos
from database import db

class TiposRepository:

    def __init__(self) -> None:
        self.TIPOSdao = TIPOSdao()

    def get_tipo(self, id):
        return self.TIPOSdao.get_tipo(id)
    
    def get_tipos(self):
        tipos = self.TIPOSdao.get_tipo()
        return ([tipo.toJson() for tipo in tipos])

    def add_tipo(self, name):
        return self.TIPOSdao.add_tipo(name)
    
    def mod_tipo(self, id, name):
        return self.TIPOSdao.mod_tipo(id, name)
    
    def delete_tipo(self, id):
        return self.TIPOSdao.add_tipo(id)