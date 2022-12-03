from db.database import db_session
from passlib.hash import pbkdf2_sha256
from sqlalchemy import select, text, update
from sqlalchemy.sql import select, update
from db.tables import User
#from formularios.usuarioform import RegistroUsuarioForm

#CRIA USUARIO
def create_user(username, password, email):
    insertUsuario = User(email,
                            username,
                            password)
    try:
        db_session.add(insertUsuario)
        db_session.commit()
    except:
        db_session.rollback()



def delete_user(user):
    try:
        db_session.delete(user)
        db_session.commit()
    except:
        db_session.rollback()
    
    
    
def update_user(id,username, password, email):
    try:
        db_session.execute( 
                           update(User).
                            where(User.id == id).
                            values(username=username, password=password, email=email)
                            )
        db_session.commit()
    except:
        db_session.rollback()


        
def selectAll_user():
    result = db_session.query(User.id, User.username, User.email, User.password).all()
    db_session.close()
    return result



def selectOne_userID(id):
    user_id =  User.query.filter_by(id=id).first()
    db_session.close()
    return user_id

 
##hbcrypt = bcrypt.hash(senha)
#comphbcrypt = bcrypt.verify(senha, hbcrypt)

#print("SENHA bcrypt :", hbcrypt)
#print("COMPARA bcrypt :",comphbcrypt)

#'$2a$12$NT0I31Sa7ihGEWpka9ASYrEFkhuTNeBQ2xfZskIiiJeyFXhRgS.Sy'
#if bcrypt.verify(senha, hbcrypt):
#        print ("PASSOU")
#else:
#        print ("It does not match") 