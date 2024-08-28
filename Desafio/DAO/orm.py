"""
        Mapeamento objeto-relacional
    Nesta classe iremos acessar o banco de dados e performar as pesquisas, utilzarei o SQLAlchemy para fazer
    o mapeamento objeto-relacional, com ele o acesso é quase direto.
"""
from sqlalchemy import create_engine
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import sessionmaker

# Cria e mapeia as tabelas do banco para classes em python
engine = create_engine("mysql+mysqlconnector://pedro:senhaTosca@localhost/anotacoes?charset=utf8mb4")
DB = automap_base()
DB.prepare(engine, reflect=True)
# Cria um objeto para abrir uma sessão com o banco
session_factory = sessionmaker(bind=engine)


class CLASSES:
    def __init__(self):
        #Criei esses objetos apenas para abreviar as chamadas a esses objeto ao longo do código
        self.classe=DB.classes.CLASSE
        self.anotacao=DB.classes.ANOTACAO
        self.imagem=DB.classes.IMAGEM

        print(DB.classes.keys())  # Imprime todas as tabelas mapeadas

        self.ses = session_factory() # Abre uma sessão com o banco para acessar a tabela CLASSE
    # Exemplo de chamada, realiza uma busca por todas as classes da tabela e retorna em uma lista
    def readAll(self):
        classes=self.ses.query(self.classe).all()
        return classes
    def readByID(self):
        pass
    def create(self):
        pass
    def update(self):
        pass
    def delete(self):
        pass
    #Destrutor para lembrar de encerrar a sessão quando finalizar
    def __del__(self):
        self.ses.close()

class ANOTACAO:
    def __init__(self):
        self.classe=DB.classes.CLASSE
        self.anotacao=DB.classes.ANOTACAO
        self.imagem=DB.classes.IMAGEM

        self.ses = session_factory()
    def readAll(self):
        anotacoes=self.ses.query(self.anotacao).all()
        return anotacoes
    def readByID(self):
        pass
    def create(self):
        pass
    def update(self):
        pass
    def delete(self):
        pass
    def __del__(self):
        self.ses.close()
class IMAGEM:
    def __init__(self):
        self.classe = DB.classes.CLASSE
        self.anotacao = DB.classes.ANOTACAO
        self.imagem = DB.classes.IMAGEM

        self.ses = session_factory()
    def readAll(self):
        imagens=self.ses.query(self.imagem).all()
        return imagens
    def readByID(self):
        pass
    def create(self):
        pass
    def update(self):
        pass
    def delete(self):
        pass
    def __del__(self):
        self.ses.close()