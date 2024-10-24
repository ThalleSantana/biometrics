from sqlalchemy import create_engine, Column, String, Integer, ForeignKey
from sqlalchemy.orm import sessionmaker, declarative_base

db = create_engine("sqlite:///meubanco.db")
Session = sessionmaker(bind=db)
session = Session()
Base = declarative_base()

class Funcionario(Base):
    __tablename__ = "funcionarios"
    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String)
    email = Column(String)
    senha = Column(String)
    cargo = Column(String)
    
    def __init__(self, nome, email, senha, cargo):
        self.nome = nome
        self.email = email
        self.senha = senha
        self.cargo = cargo

    def create(self):
        session.add(self)
        session.commit()
    
    @staticmethod
    def logar(email, senha):
        return session.query(Funcionario).filter_by(email=email, senha=senha).first()

Base.metadata.create_all(bind=db)
