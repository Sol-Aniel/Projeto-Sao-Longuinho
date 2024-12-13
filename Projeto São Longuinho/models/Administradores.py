from database import db
from email_validator import validate_email, EmailNotValidError
import bcrypt

class Administradores(db.Model):
    __tablename__ = 'administradores'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False, index=True)
    email = db.Column(db.String(255), nullable=False)
    password_hash = db.Column(db.String(255), nullable=False)

    def __repr__(self):
        return f"<Administrator {self.name}>"
    
    def toJson(self):
        return {
            "id": self.id,
            "name": self.name,
            "email": self.email,
            "password_hash": self.password_hash
        }
    
    def set_email(self, email):
        try:
            valid_email = validate_email(email)
            self.email = valid_email.email  
        except EmailNotValidError as e:
            raise ValueError(f"E-mail inválido: {e}")