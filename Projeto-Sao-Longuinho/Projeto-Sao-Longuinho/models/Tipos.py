from database import db

class Tipos(db.Model):
    __tablename__ = 'tipos'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)

    funcionarios = db.relationship('Funcionarios', back_populates='tipos')


    def __repr__(self):
        return f"<Type: {self.name}>"
    
    def toJson(self):
        return {
            "id": self.id,
            "name": self.name
        }