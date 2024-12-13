from database import db
from email_validator import validate_email, EmailNotValidError
import bcrypt

class Clientes(db.Model):
    __tablename__ = 'clientes'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False, index=True)
    email = db.Column(db.String(255))
    phone = db.Column(db.String(20))
    nacionality = db.Column(db.String(80))
    adress = db.Column(db.String(100), nullable=False)
    password_hash = db.Column(db.String(255), nullable=False)

    __table_args__ = (
        db.CheckConstraint('email IS NOT NULL OR phone IS NOT NULL', name='marque_ao_menos_uma_coluna'),
    )

    objetos = db.relationship('Objetos', back_populates='clientes', lazy=True)

    def __repr__(self):
        return f"<Client {self.name}>"
    
    def toJson(self):
        return {
            "id": self.id,
            "name": self.name,
            "email": self.email,
            "phone": self.phone,
            "nacionality": self.nacionality,
            "adress": self.adress,
            "password_hash": self.password_hash
        }
    
    def set_email(self, email):
        try:
            valid_email = validate_email(email)
            self.email = valid_email.email  
        except EmailNotValidError as e:
            raise ValueError(f"E-mail inválido: {e}")