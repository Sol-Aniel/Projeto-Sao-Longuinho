from longDAO import OBJETOSdao
from models import Objetos
from database import db

class ObjetosRepository:

    def __init__(self) -> None:
        self.OBJETOSdao = OBJETOSdao()

    def get_objeto(self, id):
        return self.OBJETOSdao.get_objeto(id)
    
    def get_objetos(self):
        return self.OBJETOSdao.get_objetos()
    
    def get_objetos_by(self, by, value):
        return self.OBJETOSdao.get_objetos_by(by, value)

    def add_objeto(self, title, photo, client_id, category_id, description, team_id, found, plural, size, weight, lost_local, lost_date, comments, price):
        return self.OBJETOSdao.add_objeto(title, photo, client_id, category_id, description, team_id, found, plural, size, weight, lost_local, lost_date, comments, price)
    
    def mod_objeto(self, id, title, photo, client_id, category_id, description, team_id, found, plural, size, weight, lost_local, lost_date, comments, price):
        return self.OBJETOSdao.mod_objeto(id, title, photo, client_id, category_id, description, team_id, found, plural, size, weight, lost_local, lost_date, comments, price)
    
    def delete_objeto(self, id):
        return self.OBJETOSdao.delete_objeto(id)

    def update_found(self, id, found):
        return self.OBJETOSdao.update_status(id, found)
    
    def update_price(self, id, price):
        return self.OBJETOSdao.update_price(id, price)
