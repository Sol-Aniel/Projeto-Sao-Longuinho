from models import Objetos
from database import db
from email_validator import validate_email, EmailNotValidError
import bcrypt

class OBJETOSdao:

    @staticmethod
    def get_objeto(id):
        return Objetos.query.get(id)

    @staticmethod
    def get_objetos():
        return Objetos.query.all()

    @staticmethod
    def get_objetos_by(by, value):
        return Objetos.query.filter(getattr(Objetos, by) == value).all()
    
    @staticmethod
    def add_objeto(title, photo, client_id, category_id, description, team_id, found, plural, size, weight, lost_local, lost_date, comments):
        try:
            objeto = Objetos(title = title, photo = photo, client_id = client_id, category_id = category_id, description = description, team_id = team_id, found = found, plural = plural, size = size, weight = weight, lost_local = lost_local, lost_date = lost_date, comments = comments)
            db.session.add(objeto)
            db.session.commit()
            return True
        except Exception as e:
            db.session.rollback()
            return e
        
    @staticmethod
    def delete_objeto(id):
        try:
            objeto = OBJETOSdao.get_objeto(id)
            db.session.delete(objeto)
            db.session.commit()
            return True
        except Exception as e:
            db.session.rollback()
            return e

    @staticmethod
    def mod_objeto(id, title, photo, client_id, category_id, description, team_id, found, plural, size, weight, lost_local, lost_date, comments):
        try:
            objeto = OBJETOSdao.get_objeto(id)  
            objeto.id = id
            objeto.title = title
            objeto.photo = photo
            objeto.client_id = client_id
            objeto.category_id = category_id
            objeto.description = description
            objeto.team_id = team_id
            objeto.found = found
            objeto.plural = plural
            objeto.size = size
            objeto.weight = weight
            objeto.lost_local = lost_local
            objeto.lost_date = lost_date
            objeto.comments = comments
            db.session.commit()
            return True
        except Exception as e:
            db.session.rollback()
            return e

    @staticmethod
    def update_found(id, found):
        try:
            objeto = OBJETOSdao.get_objeto(id)
            objeto.found = found  # True para 'achado', False para 'pendente'
            db.session.commit()
            return True
        except Exception as e:
            db.session.rollback()
            return e
