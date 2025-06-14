import sqlalchemy 

from Models.cliente import Base

engine = sqlalchemy.create_engine('sqlite:///banco.db')
connection = engine.connect()

def criar_banco():
    Base.metadata.create_all(engine)