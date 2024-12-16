from longDAO import CLIENTESdao
from models import Clientes
from database import db

class ClientesRepository:

    def __init__(self) -> None:
        self.CLIENTESdao = CLIENTESdao()

    def get_cliente(self, id):
        return self.CLIENTESdao.get_cliente(id)
    
    def get_clientes(self):
        return self.CLIENTESdao.get_cliente()
    
    def get_clientes_by(self, by, value):
        return self.CLIENTESdao.get_clientes_by(by, value)
    
    def check_password(self, password, password_hash):
        return self.CLIENTESdao.check_password(password, password_hash)

    def add_cliente(self, name, email, phone, nacionality, adress, password):
        return self.CLIENTESdao.add_cliente(name, email, phone, nacionality, adress, password)
    
    def mod_cliente(self, id, name, email, phone, nacionality, adress, password):
        return self.CLIENTESdao.mod_cliente(id, name, email, phone, nacionality, adress, password)
    
    def delete_cliente(self, id):
        return self.CLIENTESdao.add_cliente(id)