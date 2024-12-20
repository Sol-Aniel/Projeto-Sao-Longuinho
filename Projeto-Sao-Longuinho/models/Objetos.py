from database import db
import base64

class Objetos(db.Model):
    __tablename__ = 'objetos'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120), nullable=False, index=True)
    photo = db.Column(db.LargeBinary, nullable=False)
    client_id = db.Column(db.Integer, db.ForeignKey('clientes.id'), nullable=False, index=True)
    category_id = db.Column(db.Integer, db.ForeignKey('categorias.id'), nullable=False, index=True)
    description = db.Column(db.Text, nullable=False)
    team_id = db.Column(db.Integer,db.ForeignKey('equipes.id'))
    found = db.Column(db.Boolean, nullable=False, default=False, index=True)
    plural = db.Column(db.Boolean, nullable=False, default=False, index=True)
    size = db.Column(db.Float, nullable=False, default=(0))
    weight = db.Column(db.Float, nullable=False, default=(0))
    lost_local = db.Column(db.String(100), default='Não informado')
    lost_date = db.Column(db.Date, default='Não informado')
    comments = db.Column(db.Text, default='')
    price = db.Column(db.Numeric(scale=2), nullable=True)

    clientes = db.relationship('Clientes', back_populates='objetos')
    categorias = db.relationship('Categorias', back_populates='objetos')
    equipes = db.relationship('Equipes', back_populates='objetos')

    def __repr__(self):
        return f"<Object {self.title}>"
    
    def toJson(self):
        return {
            "id": self.id,
            "title": self.title,
            "photo": base64.b64encode(self.photo).decode('utf-8'),
            "client_id": self.client_id,
            "category_id": self.category_id,
            "description": self.description,
            "team": self.team,
            "found": self.found,
            "plural": self.plural,
            "size": self.size,
            "weight": self.weight,
            "lost_local": self.lost_local,
            "lost_date": self.lost_date,
            "comments": self.comments,
        }