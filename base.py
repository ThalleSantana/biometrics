from sqlalchemy import create_engine, Column, String, Integer, ForeignKey
from sqlalchemy.orm import sessionmaker, declarative_base

# Criação do banco de dados
db = create_engine("sqlite:///meubanco.db")
Session = sessionmaker(bind=db)
session = Session()
Base = declarative_base()

class Funcionario(Base):
    
  # Especifação do banco de dados, nome e colunas do banco de dados
  __tablename__ = "funcionarios"
  id = Column(Integer, primary_key=True, autoincrement=True)
  nome = Column(String)
  email = Column(String)
  senha = Column(String)
  cargo = Column(String)
  biometria = Column(String)
    
  def __init__(self, nome, email, senha, cargo, biometria):
    self.nome = nome
    self.email = email
    self.senha = senha
    self.cargo = cargo
    self.biometria = biometria

  # Função de insert no banco de dados 
  def create(self):
    session.add(self)
    session.commit()

  # Função de select no banco de dados
  @staticmethod
  def logar(email, senha):
    return session.query(Funcionario).filter_by(email=email, senha=senha).first()

Base.metadata.create_all(bind=db)

class Infos():
  data = [
    {
      "Nível 1": {
        "ID da Propriedade": 11234,
        "Proprietário": "João da Silva",
        "Localização": "Primavera, Goiás",
        "Cultura Principal": "Soja",
        "Agrotóxico Usado": "Paraquat",
        "Motivo do Uso": "Controle de ervas daninhas"
      },
      "Nível 2": {
        "Localização Detalhada": "A propriedade está situada ao norte de Primavera, ocupando 200 hectares, próxima ao Rio Primavera.",
        "Coordenadas": "-15.7895, -47.9253",
        "Uso de Agrotóxicos Proibidos": {
          "Produto": "Paraquat",
          "Quantidade": "50 litros mensais durante o período de cultivo",
          "Datas de Aplicação": ["10/07/2024", "24/07/2024"]
        }
      },
      "Nível 3": {
        "Infrações": {
          "Violação Identificada": "Uso do agrotóxico Paraquat, proibido pela legislação devido à sua alta toxicidade.",
          "Medidas de Controle": "Notificação enviada em 12/08/2024 para suspensão imediata do uso. Nova inspeção marcada para 05/11/2024."""
        },
        "Impacto Ambiental": {
          "Contaminação Detectada": "Presença de Paraquat em amostras do Rio Primavera, com níveis acima do limite seguro para a saúde humana e para a fauna local.",
          "Lençóis Freáticos": "Contaminação confirmada em amostras de água subterrânea coletadas a 15 metros de profundidade, próximas à propriedade.",
          "Análise Final": "As amostras indicam contaminação crescente nos recursos hídricos, representando um risco sério ao ecossistema e à saúde pública."
        }
      }
    },
    {
      "Nível 1": {
        "ID da Propriedade": 22345,
        "Proprietário": "Maria Oliveira",
        "Localização": "Veredas, Mato Grosso",
        "Cultura Principal": "Milho",
        "Agrotóxico Usado": "Glifosato",
        "Motivo do Uso": "Eliminação de ervas daninhas"
      },
      "Nível 2": {
        "Localização Detalhada": "A propriedade fica ao sul de Veredas, com 300 hectares, próxima ao Rio Verde.",
        "Coordenadas": "-13.2987, -56.5672",
        "Uso de Agrotóxicos Proibidos": {
          "Produto": "Glifosato",
          "Quantidade": "40 litros mensais durante o período de cultivo",
          "Datas de Aplicação": ["15/08/2024", "30/08/2024"]
        }
      },
      "Nível 3": {
        "Infrações": {
          "Violação Identificada": "Uso do agrotóxico Glifosato, restringido por regulamentações recentes.",
          "Medidas de Controle": "Notificação enviada em 20/09/2024 para suspensão do uso. Nova inspeção marcada para 10/11/2024."
        },
        "Impacto Ambiental": {
          "Contaminação Detectada": "Traços de Glifosato detectados em amostras do Rio Verde.",
          "Lençóis Freáticos": "Contaminação confirmada em amostras de água subterrânea a 20 metros de profundidade.",
          "Análise Final": "Indícios de contaminação crescente, representando risco ao ecossistema local."
        }
      }
    },
    {
      "Nível 1": {
        "ID da Propriedade": 33456,
        "Proprietário": "Carlos Ferreira",
        "Localização": "Campo Alegre, Paraná",
        "Cultura Principal": "Trigo",
        "Agrotóxico Usado": "Atrazina",
        "Motivo do Uso": "Controle de ervas daninhas"
      },
      "Nível 2": {
        "Localização Detalhada": "A propriedade está localizada no leste de Campo Alegre, cobrindo 150 hectares, perto do Rio Claro.",
        "Coordenadas": "-24.1234, -51.2345",
        "Uso de Agrotóxicos Proibidos": {
          "Produto": "Atrazina",
          "Quantidade": "30 litros mensais durante o período de cultivo",
          "Datas de Aplicação": ["01/09/2024", "15/09/2024"]
        }
      },
      "Nível 3": {
        "Infrações": {
          "Violação Identificada": "Uso de Atrazina, proibido devido à sua persistência no solo e na água.",
          "Medidas de Controle": "Notificação enviada em 25/09/2024 para interrupção do uso. Nova inspeção agendada para 20/11/2024."
        },
        "Impacto Ambiental": {
          "Contaminação Detectada": "Níveis elevados de Atrazina em amostras do Rio Claro.",
          "Lençóis Freáticos": "Contaminação identificada em amostras de água subterrânea a 18 metros de profundidade.",
          "Análise Final": "Contaminação significativa, colocando em risco a fauna aquática e a saúde humana."
        }
      }
    },
    {
      "Nível 1": {
        "ID da Propriedade": 44567,
        "Proprietário": "Ana Souza",
        "Localização": "Riacho Fundo, Minas Gerais",
        "Cultura Principal": "Café",
        "Agrotóxico Usado": "Metomil",
        "Motivo do Uso": "Controle de pragas"
      },
      "Nível 2": {
        "Localização Detalhada": "A propriedade está situada no oeste de Riacho Fundo, abrangendo 250 hectares, próxima ao Rio Grande.",
        "Coordenadas": "-18.8765, -44.9876",
        "Uso de Agrotóxicos Proibidos": {
          "Produto": "Metomil",
          "Quantidade": "25 litros mensais durante o período de cultivo",
          "Datas de Aplicação": ["05/10/2024", "20/10/2024"]
        }
      },
      "Nível 3": {
        "Infrações": {
          "Violação Identificada": "Uso de Metomil, proibido por sua alta toxicidade e impacto ambiental.",
          "Medidas de Controle": "Notificação enviada em 30/10/2024 para cessação imediata do uso. Nova inspeção marcada para 25/11/2024."
        },
        "Impacto Ambiental": {
          "Contaminação Detectada": "Presença de Metomil em amostras do Rio Grande, com níveis críticos para a vida aquática.",
          "Lençóis Freáticos": "Contaminação confirmada em amostras de água subterrânea a 17 metros de profundidade.",
          "Análise Final": "Contaminação grave, representando risco alto à biodiversidade local."
        }
      }
    }
  ]


