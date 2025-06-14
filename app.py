from Models.cliente import Cliente
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


criar_cliente("kaio")

# - [ ] função que busca os clientes, usando o ORM
# - [ ] função de cria compromisso pra um cliente usando o ORM
# - [ ] Função que busca todos os compromissos de um cliente x

