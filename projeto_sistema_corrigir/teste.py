import email

from db.database import db_session, init_db
from db.tables import User

from sqlalchemy import select, create_engine, text
from sqlalchemy.orm import scoped_session, sessionmaker

#user = User.query.filter_by(username="admin").first()
#teste = dict(user)
#print (teste)
import bcrypt
from passlib.hash import bcrypt


    #form = Loginform()
    #if form.validate_on_submit():
    ##    print("USUARIO DIGITADO: ", form.usuario_login.data)
     #   print("SENHA DIGITADO: ", form.usuario_senha.data)
     #   user = db_session.query(User.id, User.email, User.username, User.password, User.is_active).filter(User.username==form.usuario_login.data, User.password==form.usuario_senha.data).one()
      #  #res1 = dict(result)
#        #user = str(res1)
 #       print("CONSULTA DO USER:    ", user)
  #      if user:
   #         login_user(user)
    #    #print("USUARIO EXISTE/SENHA CORRETA")
        #flash('Logged in successfully.')
     #       next = request.args.get('next')
            # is_safe_url should check if the url is safe for redirects.
            # See http://flask.pocoo.org/snippets/62/ for an example.
            #if not is_safe_url(next):
            #    return abort(400)
      #      return redirect(next or url_for('base'))
      #  else:
      #      print("USUARIO E SENHA  NÃO ENCONTRADO")
    #else:
    #    print(form.errors)
    #    return render_template('login.html', form=form)

#from etl.etl import listaArquivos

#listaArquivos()

#user =  User.query.filter_by(username="novo", password= "nov").first()
#p = db_session.query( User.id, User.username, User.email).\
 #                   filter(User.username=="teste").one()
#                                   cte(name="included_parts", recursive=True)
#q = dict(p) 
#print(q)
#print(user)
#print(type(q))

#Entraga resultado em inteiro SCALAR
 
 #q = db_session.query( User.id, User.username, User.email).\
 #                   filter(User.username=="teste").scalar()
 
from sqlalchemy.sql import select
from usuario.usuarioCRUD import selectAll_user

#selectAll_user()


#user =  User.query.filter_by(id="6").first()
#user = db_session.query(User.id, User.username, User.email, User.password).filter(User.id=="1").one()#scalar()
#
# 
# 
# user = db_session.query( User.id, User.username, User.email).\
#                    filter(User.id=="5").one()
#print(user)

#from sqlalchemy import select, update#

#id=7
#user = db_session.query( User.id, User.username, User.email, User.password).\
                    #filter(User.id==id).one()
#user.username="teste"
#db_session.commit

              
from sqlalchemy import select, text, update
from sqlalchemy.sql import select, update



#db_session.execute(
#    update(User).
#    where(User.id == "6").
#    values(username="teste", password="senhateste", email="asss@rmail.com")
#    )
#db_session.commit()

#from usuario.usuarioCRUD import update_user

#id = 7
#username = "Flavio Teste"



###TESTE DE SENHA
#password = "Commit"
#email= "flavioaaaa@gmmm.com"


#update_user(id=id, username=username, password=password, email=email )
#db_session.commit()
###TESTE DE SENHA
#from passlib.hash import pbkdf2_sha256
senha = "123"
#pbkdf2_sha256
#hashpbkdf2_sha256 = pbkdf2_sha256.hash(senha)
#COMPARA E RETORNA TRUE/FALSE
#comppbkdf2_sha256 = pbkdf2_sha256.verify(senha, hashpbkdf2_sha256)
#pbkdf2_sha256
#print("SENHA pbkdf2_sha256 :",hashpbkdf2_sha256)
#print("COMPARA pbkdf2_sha256 :",comppbkdf2_sha256)



user1 = "admin"
senha1 = "admin"        
#user =  User.query.filter_by(username= user1, password=  senha1).first()
user =  User.query.filter_by(username= user1).first()
if user:
    print("USUARIO EXISTE:", user)
    if bcrypt.verify(senha1, user.password):
        print("SENHA CORRETA", senha1)
    else:
        print("SENHA INCORRETA", user.password)  
  
else:
    print("USUARIO NÃO ENCONTRADO!!!!", user)    
#    if bcrypt.verify(senha1, user.password):
#        print(user)        
