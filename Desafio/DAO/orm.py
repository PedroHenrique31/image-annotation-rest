"""
        Mapeamento objeto-relacional
    Nesta classe iremos acessar o banco de dados e performar as pesquisas, utilzarei o SQLAlchemy para fazer
    o mapeamento objeto-relacional, com ele o acesso é quase direto.
"""
from sqlalchemy import create_engine
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import sessionmaker

class ObjetoBanco:
    def __init__(self):
        # Cria e mapeia as tabelas do banco para classes em python
        engine = create_engine("mysql+mysqlconnector://pedro:senhaTosca@localhost/anotacoes?charset=utf8mb4")
        DB = automap_base()
        DB.prepare(engine, reflect=True)

        #print(DB.classes.keys()) # Mostra os nomes de todas as tabelas mapeadas

        #Criei esses objetos apenas para abreviar as chamadas a esses objeto ao longo do código
        self.classe=DB.classes.classe
        self.anotacao=DB.classes.anotacao
        self.imagem=DB.classes.imagem

        # Cria um objeto para abrir uma sessão com o banco
        session_factory = sessionmaker(bind=engine)
        self.ses = session_factory()  # Abre uma sessão com o banco para acessar a tabela


class CLASSE(ObjetoBanco):
    def __init__(self):
        super().__init__()

    # Exemplo de chamada, realiza uma busca por todas as classes da tabela e retorna em uma lista
    def readAll(self):
        classes=self.ses.query(self.classe).all()
        return classes
    def readByID(self,id):
        classe=self.ses.query(self.classe).filter_by(COD=id).first()
        return classe
    def create(self,classe):
        self.ses.add(classe)
        self.ses.commit()
    def update(self):
        pass
    def delete(self):
        pass
    #Destrutor para lembrar de encerrar a sessão quando finalizar
    def __del__(self):
        self.ses.close()

class ANOTACAO(ObjetoBanco):
    def __init__(self):
        super().__init__()
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
class IMAGEM(ObjetoBanco):
    def __init__(self):
        super().__init__()
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