from Models.cliente import Cliente, Compromisso
from orm import engine
from orm import criar_banco
from sqlalchemy.orm import Session


print("Criando Banco...")
criar_banco()
print("banco de dados criado com sucesso !!")


def criar_cliente(nome):
    with Session(engine) as session:
        cliente = Cliente(name=nome)
        session.add(cliente)
        session.commit()


# - [ ] função que busca os clientes, usando o ORM
def buscar_clientes():
    with Session(engine) as session:
        clientes = session.query(Cliente).all()
        for cliente in clientes:
            print(f"ID: {cliente.id}, Nome: {cliente.name}")

# - [ ] função de cria compromisso pra um cliente usando o ORM
def criar_compromisso(descricao, cliente_id):
    with Session(engine) as session:
        comprimisso = Compromisso(descricao=descricao, cliente_id=cliente_id)
        session.add(comprimisso)
        session.commit()

# - [ ] Função que busca todos os compromissos de um cliente x
def buscar_compromisso(cliente_id):
    with Session(engine) as session:
        compromissos = session.query(Compromisso).where(Cliente.id == cliente_id)
        for compromisso in compromissos:
            print(f"ID: {compromisso.id}, Descrição: {compromisso.descricao}")

criar_cliente("kaio")
criar_compromisso("teste", 1)
buscar_clientes()
buscar_compromisso(1)



