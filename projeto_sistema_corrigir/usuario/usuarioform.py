from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, IntegerField
from wtforms.validators import DataRequired, Length
from wtforms.csrf.session import SessionCSRF
from wtforms import ValidationError


class LoginForm(FlaskForm):
   # email = StringField('email', validators=[DataRequired()])
    username = StringField('username', validators=[DataRequired()])
    password = StringField('password', validators=[DataRequired()])
    
class RegistroUsuarioForm(FlaskForm):
    #id = StringField('id', validators=[DataRequired()])
    email = StringField('email', validators=[DataRequired()])
    username = StringField('username', validators=[DataRequired()])
    password = StringField('password', validators=[DataRequired()])

class DeleteUsuarioForm(FlaskForm):
    id = IntegerField('id', validators=[DataRequired()])

class UpdateUsuarioForm(FlaskForm):
    id = StringField('id', validators=[DataRequired()])
    email = StringField('email', validators=[DataRequired()])
    username = StringField('username', validators=[DataRequired()])
    password = StringField('password', validators=[DataRequired()])