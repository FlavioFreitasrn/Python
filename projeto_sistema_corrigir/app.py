#import pacotes
from wsgiref import validate
from flask import Flask, render_template, redirect, url_for, abort, request, flash
from flask_login import LoginManager, login_user, login_required, logout_user
#import bcrypt
from passlib.hash import bcrypt
from flask_wtf.csrf import CSRFProtect
from flask_wtf.csrf import CSRFError
from sqlalchemy import select, text, update
from sqlalchemy.sql import select, update
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
#import internos
from db.database import db_session, engine, init_db
from db.tables import User
from usuario.usuarioCRUD import selectAll_user, create_user, delete_user, update_user
from usuario.usuarioform import LoginForm, RegistroUsuarioForm, DeleteUsuarioForm, UpdateUsuarioForm
from admin.modelview import UserView

#Flask
app = Flask(__name__)
app.config.from_object("config")

#Flask-Adamin
admin = Admin(app, name="EstudoPY", template_mode='bootstrap3')
admin.add_view(UserView(User, db_session))


#CSRF Protection
csrf = CSRFProtect()
csrf.init_app(app)



#Flask-login
login_manager = LoginManager()
login_manager.init_app(app)



@login_manager.user_loader
def load_user(user_id):
    id = User.query.get(int(user_id))
    db_session.close()
    #return User.query.get(int(user_id))
    return id



@app.errorhandler(CSRFError)
def handle_csrf_error(e):
    return render_template('csrf_error.html', reason=e.description), 400



#Rotas
@app.route("/")
def index():
    return redirect(url_for("login"))



@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        #user =  User.query.filter_by(username=form.username.data, password=  form.password.data).first()
        user =  User.query.filter_by(username=form.username.data).first()
        if user:
            print("USUARIO EXISTE:", user)
            if bcrypt.verify(form.password.data, user.password):
                print("SENHA CORRETA", form.password.data)
                
                login_user(user, remember=True)
                user.authenticated = True
                return render_template("base.html", form=form)
            else:
                print("SENHA INCORRETA", user.password)
                
        else:
            print("USUARIO NÃO ENCONTRADO!!!!", user) 
            return render_template("login.html", form=form)
    else:
        return render_template("login.html", form=form)



@app.route("/usuario", methods=['GET', 'POST'])
def usuario():
    result = selectAll_user()
    return render_template("usuario.html", result=result)



@app.route("/usuarioregistro", methods=['GET', 'POST'])
@csrf.exempt
def usuarioregistro():
    form_reg = RegistroUsuarioForm()
    return render_template("usuarioregistro.html", form=form_reg)



@app.route("/usuariosalvar", methods=['GET', 'POST'])
#@csrf.exempt
def usuariosalvar():
    form_reg = RegistroUsuarioForm()
    if form_reg.validate_on_submit():
        user =  User.query.filter_by(username=form_reg.username.data, password= form_reg.password.data).first()
        if user:
            return redirect(url_for("usuarioregistro", form= form_reg))
        else:
            create_user(username=form_reg.username.data, password= bcrypt.hash(form_reg.password.data), email= form_reg.email.data)
            return redirect(url_for("usuario", form= form_reg))
      
        
        
@app.route("/usuarioapaga/<int:id>", methods=['GET', 'POST'])
@csrf.exempt
def usuarioapaga(id):
    user =  User.query.filter_by(id=id).first()
    if user:
        delete_user(user)
        return redirect(url_for("usuario"))
    else:
        return redirect(url_for("usuario"))

 
@app.route("/usuarioeditar/<int:id>", methods=['GET', 'POST'])
@csrf.exempt
def usuarioeditar(id):
    form_update = UpdateUsuarioForm()
    user = db_session.query( User.id, User.username, User.email, User.password).\
                    filter(User.id==id).one()
    if user:
            form_update.id.data = str(user.id)
            form_update.username.data = str(user.username)
            form_update.email.data = str(user.email)
            form_update.password.data = str(user.password)
            return render_template("usuarioeditform.html", form=form_update)
    else:
        return redirect(url_for("usuario", form= form_update))   
    


#@app.route("/usuarioeditarsalvar/<form_update>", methods=['GET', 'POST'])
@app.route("/usuarioeditarsalvar/<int:id>", methods=['GET', 'POST'])
#@csrf.exempt
def usuarioeditarsalvar(id):
    form_update = UpdateUsuarioForm()
    if form_update.validate_on_submit():
        user = db_session.query( User.id, User.username, User.email, User.password).\
                    filter(User.id==id).one()
        if user and request.method == 'POST':
            update_user(id=form_update.id.data,
                    username=str(form_update.username.data),
                    #password=form_update.password.data,
                    password=bcrypt.hash(form_update.password.data),
                    email=form_update.email.data)
            return redirect(url_for("usuario", form=form_update))
    return redirect(url_for("usuario"))              


                  
@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("login"))

@app.route('/etl')
#@csrf.exempt
def etl():
    return render_template("etl.html")
    #return redirect('etl.html')
    #return redirect(url_for("etl.html"))
@app.route('/admin')
#@csrf.exempt
def admin():
    #return render_template("etl.html")
    #return redirect('etl.html')
    return redirect(url_for("admin"))

if __name__ == '__main__':
   app.run()