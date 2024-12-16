from database import db

class Equipes(db.Model):
    __tablename__ = 'equipes'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)

    objetos = db.relationship('Objetos', back_populates='equipes')
    funcionarios = db.relationship('Funcionarios', back_populates='equipes')

    def __repr__(self):
        return f"<Team: {self.name}>"
    
    def toJson(self):
        return {
            "id": self.id,
            "name": self.name
        }