from longDAO import FUNCdao
from models import Funcionarios
from database import db

class FuncionariosRepository:

    def __init__(self) -> None:
        self.FUNCdao = FUNCdao()

    def get_funcionario(self, id):
        return self.FUNCdao.get_funcionario(id)
    
    def get_funcionarios(self):
        return self.FUNCdao.get_funcionarios()
    
    def get_funcionarios_by(self, by, value):
        return self.FUNCdao.get_funcionarios_by(by, value)

    def check_password(self, password, password_hash):
        return self.FUNCdao.check_password(password, password_hash)

    def add_funcionario(self, name, team_id, type_id, email, phone, salary, adress, password):
        return self.FUNCdao.add_funcionario(name, team_id, type_id, email, phone, salary, adress, password)
    
    def mod_funcionario(self, id, name, team_id, type_id, email, phone, salary, adress, password):
        return self.FUNCdao.mod_funcionario(id, name, team_id, type_id, email, phone, salary, adress, password)
    
    def delete_funcionario(self, id):
        return self.FUNCdao.add_funcionario(id)
    
    def update_equipe(self, id, equipe_id):
        return self.FUNCdao.update_equipe(id, equipe_id)