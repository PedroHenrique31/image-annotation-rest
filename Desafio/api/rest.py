from flask_restful import Resource, request
from flask import jsonify,send_file
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema

import DAO.orm
from DAO import *

"""
 Dando seguimento a criação da API, vamos usar o módulo flask_restful para implementar a API e o 
 JSONFIY para serializar.
"""
dadosClasse=DAO.orm.CLASSE()

class classeSchema(SQLAlchemyAutoSchema):
    class Meta:
        model=dadosClasse.classe


class ClasseRest(Resource):
    def __init__(self):
        self.campos=['COD','CLASSE']
    def get(self):
        pass
    def post(self):
        pass
    def put(self):
        pass
    def delete(self):
        pass

