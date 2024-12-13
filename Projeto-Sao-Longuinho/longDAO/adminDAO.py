from models import Administradores
from database import db
from email_validator import validate_email, EmailNotValidError
import bcrypt

class ADMINdao:

    @staticmethod
    def get_admin(id):
        Administradores.query.get(id)

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
    def add_admin(name, email, password):
        try:
            email_ = ADMINdao.set_email(email)
            password_ = ADMINdao.set_password(password)
            admin = Administradores(name=name, email=email_, password_hash=password_)
            db.session.add(admin)
            db.session.commit()
            return True
        except Exception as e:
            db.session.rollback()
            return e