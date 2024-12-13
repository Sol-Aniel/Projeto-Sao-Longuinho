from database import db
from email_validator import validate_email, EmailNotValidError
import bcrypt

class Funcionarios(db.Model):
    __tablename__ = 'funcionarios'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False, index=True)
    team_id = db.Column(db.String(50),db.ForeignKey('equipes.id'), nullable=False, default='')
    type_id = db.Column(db.Integer, db.ForeignKey('tipos.id'), nullable=False, index=True)
    email = db.Column(db.String(255), nullable=False)
    phone = db.Column(db.String(20), nullable=False)
    salary = db.Column(db.Float, nullable=False)
    adress = db.Column(db.String(100), nullable=False)
    password_hash = db.Column(db.String(255), nullable=False)

    objetos = db.relationship('Objetos', back_populates='funcionarios', lazy=True)
    equipes = db.relationship('Equipes', backpopulates='funcionarios')
    tipos = db.relationship('Tipos', backpopulates='funcionarios')

    def __repr__(self):
        return f"<Worker {self.name}>"
    
    def toJson(self):
        return {
            "id": self.id,
            "name": self.name,
            "team_id": self.team_id,
            "type_id": self.type_id,
            "email": self.email,
            "phone": self.phone,
            "salary": self.salary,
            "adress": self.adress,
            "password_hash": self.password_hash
        }
    
    def set_email(self, email):
        try:
            valid_email = validate_email(email)
            self.email = valid_email.email  
        except EmailNotValidError as e:
            raise ValueError(f"E-mail inválido: {e}")