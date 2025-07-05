from cliente_repositorio import ClienteRepository
from orm import criar_banco
from sqlalchemy.orm import Session


print("Criando Banco...")
criar_banco()
print("banco de dados criado com sucesso !!")

ClienteRepository.buscar()


