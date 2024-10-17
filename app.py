from sqlalchemy import create_engine, Column, String, Integer, Boolean, ForeignKey
from sqlalchemy.orm import sessionmaker, declarative_base


db = create_engine("sqlite:///meubanco.db")
Session = sessionmaker(bind=db)
session = Session()


Base = declarative_base()

# Lista de cargos disponíveis
CARGOS_DISPONIVEIS = ["Gerente", "Desenvolvedor", "Estagiário"]




# a tabelas
class Funcionario(Base):
    __tablename__ = "funcionarios"

    id = Column("id", Integer, primary_key=True, autoincrement=True)
    nome = Column("nome", String)
    email = Column("email", String)
    senha = Column("senha", String)
    cargo = Column("cargo", String)
    #biometria = Column("biometria", String)

    def __init__(self, nome, email, senha, cargo):
        self.nome = nome
        self.email = email
        self.senha = senha
        self.cargo = cargo
        #self.biometria = biometria



Base.metadata.create_all(bind=db)

#Tela inicial -- começa aqui

login = str(input('Deseja logar ou criar uma conta?\n\n A) Logar \n B) Criar \n\n')) .lower()

if login == 'a':
    print("\nVocê escolheu logar.\n")

    # Solicitando as infos para entrar
    email_login = str(input("Digite o seu email: "))
    senha_login = str(input("Digite a sua senha: "))
    
    # Verificando se o email e/ou a senha existem no banco de dados
    funcionario = session.query(Funcionario).filter_by(email=email_login, senha=senha_login).first()
    
    if funcionario:
        print(f"Login bem-sucedido! Bem-vindo(a), {funcionario.nome}.")
    # Exibindo informações baseadas no cargo, sendo Estag n1, Desenv n2 e Gerente n3 como na documentação da APS
        if funcionario.cargo == "Estagiário":
            print("\nInformações para Estagiário:\n")
            print("1. Monitorar as propriedades rurais que utilizam agrotóxicos. Priorize áreas com risco moderado.")
            print("2. Relatórios de uso de agrotóxicos podem ser solicitados por desenvolvedores ou gerentes.")
        
        elif funcionario.cargo == "Desenvolvedor":
            print("\nInformações para Desenvolvedor:\n")
            print("1. Desenvolver novas soluções para rastrear propriedades rurais utilizando agrotóxicos proibidos.")
            print("2. Criar uma análise de impacto dos agrotóxicos proibidos nos lençóis freáticos de regiões específicas.")
            print("3. Coordenar com os estagiários para obter relatórios de campo.")

        elif funcionario.cargo == "Gerente":
            print("\nInformações para Gerente:\n")
            print("1. Acesso total aos dados estratégicos das propriedades rurais que utilizam agrotóxicos proibidos.")
            print("2. Revisar e aprovar relatórios de impacto ambiental, especialmente em áreas de grande risco para os lençóis freáticos.")
            print("3. Gerenciar ações de controle de uso de agrotóxicos, atuando diretamente com os órgãos reguladores.")
            print("4. Planejar ações de mitigação para reduzir a contaminação de rios e mares causada por esses produtos.")


    else:
        print("Email ou senha incorretos. Tente novamente.")

elif login == 'b':
    print("Você escolheu criar uma conta.")
    # Exibindo as opções de cargo para o usuário
    print("-- Cargos disponíveis --:")
    for cargo in CARGOS_DISPONIVEIS:
      print(f"- {cargo}")
    

    print("-------------------------")

    #Dados do usuario que serão posteriormente inseridos no banco
    nome1 = str(input('Digite o seu nome: '))
    email1 = str(input('Digite um email: '))
    senha1 = str(input('Digite uma senha: '))
    
    #como puxar a biometria?

    while True:
        cargo1 = str(input('Digite o seu cargo: '))
        if cargo1 in CARGOS_DISPONIVEIS:
            break
        print("Cargo inválido. Tente novamente.")

    print("\n \nConta criada \n")
    
    # C - Create
    funcionario = Funcionario(nome=nome1, email=email1, senha=senha1, cargo=cargo1)
    session.add(funcionario)
    session.commit()





    

else:
    print("Opção inválida. Escolha A ou B.")
   






