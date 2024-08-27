"""
        Mapeamento objeto-relacional
    Nesta classe iremos acessar o banco de dados e performar as pesquisas, utilzarei o SQLAlchemy para fazer
    o mapeamento objeto-relacional, com ele o acesso é quase direto.
"""
from sqlalchemy import create_engine
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import sessionmaker

engine = create_engine("mysql+mysqlconnector://pedro:senhaTosca@localhost/myversion_cawa_model?charset=utf8mb4")
DB = automap_base()
DB.prepare(engine, reflect=True)

