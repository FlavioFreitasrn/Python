from re import T
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

#ENGINE
#engine = create_engine("sqlite:///estudopy/db/db_estudopy.db", echo = True)
engine = create_engine("sqlite+pysqlite:///estudopy/db/db_estudopy.db", echo = True, future=True)

#SESSION
db_session = scoped_session(sessionmaker(autocommit = False,
                                         autoflush = False,
                                         bind = engine))


#DECLARATIVE
Base = declarative_base()
Base.query = db_session.query_property()

#CRIA AS TABELAS NO BANCO
def init_db():
    import db.tables
    Base.metadata.create_all(bind=engine)
    print("Tabelas Criadas com sucesso")
    