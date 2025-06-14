from typing import List

from sqlalchemy.orm import DeclarativeBase, Mapped
from sqlalchemy.orm import relationship, mapped_column

from sqlalchemy import String, Boolean, ForeignKey # Objeto base de banco de dados


class Base(DeclarativeBase):
    pass

class Cliente(Base):
    __tablename__ = "clientes"
    
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(30))
    
    
    
    
    compromissos: Mapped[List["Compromisso"]] = relationship(back_populates= "cliente")

class Compromisso(Base):
    __tablename__ = "compromissos"
    
    id: Mapped[int] = mapped_column(primary_key=True)
    descricao: Mapped[str] = mapped_column(String(256))
    completo: Mapped[bool] = mapped_column(Boolean(), default= False)
    
    cliente_id: Mapped[int] = mapped_column(ForeignKey("clientes.id"))
    # Cria uma relação, com o campo "compromissos" do Clinte
    cliente: Mapped["Cliente"] = relationship(back_populates= "compromisso")