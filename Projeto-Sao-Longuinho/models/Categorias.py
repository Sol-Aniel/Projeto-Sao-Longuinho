from database import db

class Categorias(db.Model):
    __tablename__ = 'categorias'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)

    objetos = db.relationship('Objetos', back_populates='categorias')


    def __repr__(self):
        return f"<Category: {self.name}>"
    
    def toJson(self):
        return {
            "id": self.id,
            "name": self.name
        }