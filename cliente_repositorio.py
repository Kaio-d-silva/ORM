from sqlalchemy.orm import Session
from orm import engine
from Models.models import Cliente

class ClienteRepository: 
    @staticmethod
    def criar(nome):
        with Session(engine) as session:
            cliente = Cliente(name=nome)
            session.add(cliente)
            session.commit()


    @staticmethod
    def buscar():
        with Session(engine) as session:
            clientes = session.query(Cliente).all()
            for cliente in clientes:
                print(f"ID: {cliente.id}, Nome: {cliente.name}")

