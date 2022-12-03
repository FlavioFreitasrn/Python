from flask_login import UserMixin
from sqlalchemy.orm import column_property
from sqlalchemy.orm import relationship, backref
from sqlalchemy import Boolean, DateTime, Column, Integer, String, ForeignKey
#importes internos
from db.database import Base
#FLAK-LOGIN - USUARIO DO SISTEMA


class User(Base, UserMixin):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    email = Column(String(255), unique=True)
    username = Column(String(255))
    password = Column(String(255))
    last_login_at = Column(DateTime())
    current_login_at = Column(DateTime())
    last_login_ip = Column(String(100))
    current_login_ip = Column(String(100))
    login_count = Column(Integer)
    active = Column(Boolean())
    confirmed_at = Column(DateTime())
    
    def __init__(self, email, username, password):
        self.email = email
        self.username = username
        self.password = password

    #roles = relationship('Role', secondary='roles_users',
    #                     backref=backref('users', lazy='dynamic'))
     # Flask-Login integration
    # NOTE: is_authenticated, is_active, and is_anonymous
    # are methods in Flask-Login < 0.3.0
    @property
    def is_authenticated(self):
        return True

    @property
    def is_active(self):
        return True

    @property
    def is_anonymous(self):
        return False

    def get_id(self):
        return str(self.id)

    # Required for administrative interface
    def __str__(self):
        return self.username
        
    
    #def __repr__(self):
    #    return (self.id, self.username, self.email)
