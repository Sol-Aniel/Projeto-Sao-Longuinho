from longDAO import FUNCdao
from models import Funcionarios
from database import db

class FuncionariosRepository:

    def __init__(self) -> None:
        self.FUNCdao = FUNCdao()

    def get_funcionario(self, id):
        return self.FUNCdao.get_funcionario(id)
    
    def get_funcionarios(self):
        funcionarios = self.FUNCdao.get_funcionario()
        return ([funcionario.toJson() for funcionario in funcionarios])
    
    def get_funcionarios_by(self, by, value):
        return self.FUNCdao.get_funcionarios_by(by, value)
    
    def get_func_by_id(self, id):
        listafunc = []
        listafunc.extend([self.funcDao.get_func_by_id(id)])
        funcjson = []
        for funcionario in listafunc:
            funcjson.extend([funcionario.toJson()])
            equipes = self.equipesDao.get_equipe(funcionario.team_id)
            tipos = self.tiposDao.get_tipo(funcionario.type_id)
            funcjson[funcionario.id-1]["equipe"] = equipes.name
            funcjson[funcionario.id-1]["tipo"] = tipos.name
        return funcjson

    def check_password(self, password, password_hash):
        return self.FUNCdao.check_password(password, password_hash)

    def add_funcionario(self, name, team_id, type_id, email, phone, salary, adress, password):
        return self.FUNCdao.add_funcionario(name, team_id, type_id, email, phone, salary, adress, password)
    
    def mod_funcionario(self, id, name, team_id, type_id, email, phone, salary, adress, password):
        return self.FUNCdao.mod_funcionario(id, name, team_id, type_id, email, phone, salary, adress, password)
    
    def delete_funcionario(self, id):
        return self.FUNCdao.add_funcionario(id)