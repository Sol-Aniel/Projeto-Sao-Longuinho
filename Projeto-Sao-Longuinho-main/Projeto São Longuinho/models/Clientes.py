from database import db
from email_validator import validate_email, EmailNotValidError
import bcrypt

class Clientes(db.Model):
    __tablename__ = 'autores'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False, index=True)
    email = db.Column(db.String(255))
    phone = db.Column(db.String(20))
    nacionality = db.Column(db.String(80))
    birth_date = db.Column(db.Date, nullable=False)
    password_hash = db.Column(db.String(255), nullable=False)

    __table_args__ = (
        db.CheckConstraint('email IS NOT NULL OR phone IS NOT NULL', name='marque_ao_menos_uma_coluna'),
    )

    objetos = db.relationship('Objetos', back_populates='clientes', lazy=True)

    def __repr__(self):
        return f"<Author {self.name}>"
    
    def toJson(self):
        return {
            "id": self.id,
            "name": self.name,
            "nacionality": self.nacionality,
            "birth_date": self.birth_date,
        }