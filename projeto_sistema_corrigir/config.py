#FLASK
DEBUG = True
#HOST= '192.168.0.2'
#PORT=80
#SERVER_NAME = '192.168.0.2:5000'

#FLASK SECURITY
SECRET_KEY = 'super-secret'
SECURITY_PASSWORD_HASH = 'bcrypt'
SECURITY_PASSWORD_SALT= '$2a$16$PnnIgfMwkOjGX4SkHqSOPO'
# WTForms
#WTF_CSRF_TIME_LIMIT = None
WTF_CSRF_ENABLED = True
WTF_CSRF_SECRET_KEY = 'super-secret'
##FLASK-ADMIN
FLASK_ADMIN_SWATCH = 'cerulean'


#Flask-Security - LOGIN
#SECURITY_LOGIN_USER_TEMPLATE = 'login_user.html'
#SECURITY_LOGIN_URL = '/templates/security/login'
#SECURITY_CHANGEABLE = True

#Flask-Security - Registro 
#SECURITY_REGISTERABLE = True
#SECURITY_REGISTER_URL = '/register'
#SECURITY_REGISTER_USER_TEMPLATE = 'register_user.html'
#SECURITY_SEND_REGISTER_EMAIL = False

#CONFIGURAÇÃO EMAIL
#app.config['MAIL_SERVER'] = "smtp.example.com"
#app.config['MAIL_PORT'] = 465
#app.config['MAIL_USE_TLS'] = True
#app.config['MAIL_USERNAME'] = 'username'
#app.config['MAIL_PASSWORD'] ='password'
#app.config['MAIL_DEFAULT_SENDER'] = MAIL_DEFAULT_SENDER
#appMail = Mail()
#appMail.init_app(app)