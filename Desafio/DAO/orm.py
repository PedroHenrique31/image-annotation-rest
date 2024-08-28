"""
        Mapeamento objeto-relacional
    Nesta classe iremos acessar o banco de dados e performar as pesquisas, utilzarei o SQLAlchemy para fazer
    o mapeamento objeto-relacional, com ele o acesso é quase direto.
"""
from sqlalchemy import create_engine
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import sessionmaker

# Cria e mapeia as tabelas do banco para classes em python
engine = create_engine("mysql+mysqlconnector://pedro:senhaTosca@localhost/myversion_cawa_model?charset=utf8mb4")
DB = automap_base()
DB.prepare(engine, reflect=True)
# Cria um objeto para abrir uma sessão com o banco
session_factory = sessionmaker(bind=engine)

class CLASSE:
    def __init__(self):
        #Criei esses objetos apenas para abreviar as chamadas a esses objeto ao longo do código
        self.classe=DB.classes.CLASSE
        self.anotacao=DB.classes.ANOTACAO
        self.imagem=DB.classes.IMAGEM

        self.ses = session_factory() # Abre uma sessão com o banco para acessar a tabela CLASSE
    # Exemplo de chamada, realiza uma busca por todas as classes da tabela e retorna em uma lista
    def readAll(self):
        classes=self.ses.query(self.classe).all()
        return classes

