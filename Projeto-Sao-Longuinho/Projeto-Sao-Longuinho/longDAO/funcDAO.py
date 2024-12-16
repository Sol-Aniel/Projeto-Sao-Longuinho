from models import Funcionarios
from database import db
from email_validator import validate_email, EmailNotValidError
import bcrypt

class FUNCdao:

    @staticmethod
    def get_funcionario(id):
        Funcionarios.query.get(id)

    @staticmethod
    def get_funcionarios():
        Funcionarios.query.all()

    @staticmethod
    def get_funcionarios_by(by, value):
        return Funcionarios.filter(Funcionarios.by == value).all()
    
    @staticmethod
    def get_func_by_id(id):
        return Funcionarios.query.get(id)

    @staticmethod
    def set_email(email):
        try:
            valid_email = validate_email(email)
            return valid_email.email  
        except EmailNotValidError as e:
            raise ValueError(f"E-mail inválido: {e}")
        
    @staticmethod
    def set_password(password):
        salt = bcrypt.gensalt()  
        hashed = bcrypt.hashpw(password.encode('utf-8'), salt) 
        password_hash = hashed.decode('utf-8') 
        return password_hash 
    
    @staticmethod
    def check_password(password, password_hash):
        return bcrypt.checkpw(password.encode('utf-8'), password_hash.encode('utf-8'))
    
    @staticmethod
    def add_funcionario(name, team_id, type_id, email, phone, salary, adress, password):
        try:
            email_ = FUNCdao.set_email(email)
            password_ = FUNCdao.set_password(password)
            funcionario = Funcionarios(name=name, team_id=team_id, type_id=type_id, email=email_, phone=phone, salary=salary, adress=adress, password_hash=password_)
            db.session.add(funcionario)
            db.session.commit()
            return True
        except Exception as e:
            db.session.rollback()
            return e
        
    @staticmethod
    def delete_funcionario(id):
        try:
            funcionario = FUNCdao.get_funcionario(id)
            db.session.delete(funcionario)
            db.session.commit()
            return True
        except Exception as e:
            db.session.rollback()
            return e

    @staticmethod
    def mod_funcionario(id, name, team_id, type_id, email, phone, salary, adress, password):
        try:
            email_ = FUNCdao.set_email(email)
            password_ = FUNCdao.set_password(password)
            funcionario = FUNCdao.get_funcionario(id)  
            funcionario.name = name
            funcionario.email = email_
            funcionario.team_id = team_id
            funcionario.type_id = type_id
            funcionario.phone = phone
            funcionario.salary = salary
            funcionario.adress = adress
            funcionario.password_hash = password_ 
            db.session.commit()
            return True
        except Exception as e:
            db.session.rollback()
            return e