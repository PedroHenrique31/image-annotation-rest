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
        if request.args.get(self.campos[0]) is not  None:
             ## Se a solicitação de get passar o COD como argumento, chamamos a funcao readByID
            id_classe=request.args.get(self.campos[0])
            obj=dadosClasse.readByID(id_classe)
            schema=classeSchema() # Cria uma tupla com o modelo classe
            resultado=schema.dump(obj) # cria um dicionário com o modelo, um dicionario é quase um JSON
            return jsonify(resultado) # gera o JSON a partir do dicionário e retorna o resultado
        elif request.args.get(self.campos) is not None:
            pass
        else:
            pass

    def post(self):
        pass
    def put(self):
        pass
    def delete(self):
        pass
#######################################
class AnotacaoRest(Resource):
    def __init__(self):
        self.campos=[]

