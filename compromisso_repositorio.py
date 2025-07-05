from sqlalchemy.orm import Session
from orm import engine
from Models.models import Compromisso, Cliente

class CompromissoRepository:
    @staticmethod
    def criar(descricao, cliente_id):
        with Session(engine) as session:
            comprimisso = Compromisso(descricao=descricao, cliente_id=cliente_id)
            session.add(comprimisso)
            session.commit()

    @staticmethod
    def buscar(cliente_id):
        with Session(engine) as session:
            compromissos = session.query(Compromisso).where(Cliente.id == cliente_id)
            for compromisso in compromissos:
                print(f"ID: {compromisso.id}, Descrição: {compromisso.descricao}")