from models import Clientes
from database import db
from email_validator import validate_email, EmailNotValidError
import bcrypt

class CLIENTESdao:

    @staticmethod
    def get_cliente(id):
        return Clientes.query.get(id)

    @staticmethod
    def get_clientes():
        return Clientes.query.all()

    @staticmethod
    def get_clientes_by(by, value):
        return Clientes.filter(getattr(Clientes, by) == value).all()

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
    def add_cliente(name, email, phone, nacionality, adress, password):
        try:
            email_ = CLIENTESdao.set_email(email)
            password_ = CLIENTESdao.set_password(password)
            cliente = Clientes(name=name, email=email_, phone=phone, nacionality=nacionality, adress=adress, password_hash=password_)
            db.session.add(cliente)
            db.session.commit()
            return True
        except Exception as e:
            db.session.rollback()
            return e
        
    @staticmethod
    def delete_cliente(id):
        try:
            cliente = CLIENTESdao.get_cliente(id)
            db.session.delete(cliente)
            db.session.commit()
            return True
        except Exception as e:
            db.session.rollback()
            return e

    @staticmethod
    def mod_cliente(id, name, email, phone, nacionality, adress, password):
        try:
            email_ = CLIENTESdao.set_email(email)
            password_ = CLIENTESdao.set_password(password)
            cliente = CLIENTESdao.get_cliente(id)  
            cliente.name = name
            cliente.email = email_
            cliente.phone = phone
            cliente.nacionality = nacionality
            cliente.adress = adress
            cliente.password_hash = password_ 
            db.session.commit()
            return True
        except Exception as e:
            db.session.rollback()
            return e