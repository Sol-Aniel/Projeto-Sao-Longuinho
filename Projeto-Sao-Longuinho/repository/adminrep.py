from longDAO import ADMINdao
from models import Administradores
from database import db

class AdministradoresRepository:

    def __init__(self) -> None:
        self.ADMINdao = ADMINdao()

    def get_admin(self, id):
        return self.ADMINdao.get_admin(id)
    
    def get_admins(self):
        return self.ADMINdao.get_admins()
    
    def get_admin_by(self, by, value):
        return self.ADMINdao.get_admin_by(by, value)
    
    def check_password(self, password, password_hash):
        return self.ADMINdao.check_password(password, password_hash)

    def add_admin(self, name, email, password):
        return self.ADMINdao.add_admin(name, email, password)