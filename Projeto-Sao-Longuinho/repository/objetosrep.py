from longDAO import OBJETOSdao
from models import Objetos
from database import db

class ObjetosRepository:

    def __init__(self) -> None:
        self.OBJETOSdao = OBJETOSdao()

    def get_objeto(self, id):
        return self.OBJETOSdao.get_objeto(id)
    
    def get_objetos(self):
        objetos = self.OBJETOSdao.get_objeto()
        return ([objeto.toJson() for objeto in objetos])
    
    def get_objetos_by(self, by, value):
        return self.OBJETOSdao.get_objetos_by(by, value)

    def add_objeto(self, title, photo, client_id, category_id, description, team, found, plural, size, weight, lost_local, lost_date, comments):
        return self.OBJETOSdao.add_objeto(title, photo, client_id, category_id, description, team, found, plural, size, weight, lost_local, lost_date, comments)
    
    def mod_objeto(self, id, title, photo, client_id, category_id, description, team, found, plural, size, weight, lost_local, lost_date, comments):
        return self.OBJETOSdao.mod_objeto(id, title, photo, client_id, category_id, description, team, found, plural, size, weight, lost_local, lost_date, comments)
    
    def delete_objeto(self, id):
        return self.OBJETOSdao.add_objeto(id)