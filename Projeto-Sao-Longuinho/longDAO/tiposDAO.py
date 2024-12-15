from models import Tipos
from database import db

class TIPOSdao:

    @staticmethod
    def get_tipo(id):
        return Tipos.query.get(id)

    @staticmethod
    def get_tipos():
        return Tipos.query.all()
    
    @staticmethod
    def add_tipo(name):
        try:
            tipo = Tipos(name=name)
            db.session.add(tipo)
            db.session.commit()
            return True
        except Exception as e:
            db.session.rollback()
            return e
        
    @staticmethod
    def mod_tipo(id, name):
        try:
            tipo = TIPOSdao.get_tipo(id)  
            tipo.name = name
            db.session.commit()
            return True
        except Exception as e:
            db.session.rollback()
            return e
        
    @staticmethod
    def delete_tipo(id):
        try:
            tipo = TIPOSdao.get_tipo(id)
            db.session.delete(tipo)
            db.session.commit()
            return True
        except Exception as e:
            db.session.rollback()
            return e