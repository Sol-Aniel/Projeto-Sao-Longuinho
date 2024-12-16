from models import Equipes
from database import db
from email_validator import validate_email, EmailNotValidError
import bcrypt

class EQUIPESdao:

    @staticmethod
    def get_equipe(id):
        Equipes.query.get(id)

    @staticmethod
    def get_equipes():
        Equipes.query.all()

    @staticmethod
    def get_equipes_by(by, value):
        return Equipes.filter(Equipes.by == value).all()
    
    @staticmethod
    def add_equipe(name):
        try:
            equipe = Equipes(name=name)
            db.session.add(equipe)
            db.session.commit()
            return True
        except Exception as e:
            db.session.rollback()
            return e
        
    @staticmethod
    def delete_equipe(id):
        try:
            equipe = EQUIPESdao.get_equipe(id)
            db.session.delete(equipe)
            db.session.commit()
            return True
        except Exception as e:
            db.session.rollback()
            return e

    @staticmethod
    def mod_equipe(id, name):
        try:
            equipe = EQUIPESdao.get_equipe(id)  
            equipe.name = name
            db.session.commit()
            return True
        except Exception as e:
            db.session.rollback()
            return e