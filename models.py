# Estrutura das tabelas do banco

from sqlalchemy.orm import Session
from sqlalchemy import Column, Integer, String
from database import Base, engine

class Usuario(Base):
    __tablename__ = "usuarios"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)
    senha = Column(String, nullable=False)  # Senha deve ser criptografada!

Base.metadata.create_all(bind=engine)
