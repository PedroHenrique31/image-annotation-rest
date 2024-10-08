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
dadosAnotacao=DAO.orm.ANOTACAO()

class classeSchema(SQLAlchemyAutoSchema):
    class Meta:
        model=dadosClasse.classe
class anotacaoSchema(SQLAlchemyAutoSchema):
    class Meta:
        model=dadosAnotacao.anotacao


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
        # Se a solicitacao enviar o campo CLASSE, faz as pesquisa inversa
        elif request.args.get(self.campos[1]) is not None:
            pass
        # Se a solicitação não informa nenhum argumento retorna todos os dados
        else:
            lista=dadosClasse.readAll()
            schema=classeSchema(many=True) # Avisa que tem serializar muitos
            return jsonify(schema.dump(lista)) # Passa tudo pra JSON
    # Insere um novo registro de classe
    def post(self):
        obj=dadosClasse.classe() # cria um objeto do tipo classe
        obj.CLASSE=request.args.get("NOME")
        dadosClasse.create(obj)
        return jsonify({'insert':obj.COD})
    # Altera um registro de classe
    def put(self):
        obj = dadosClasse.readByID(request.args.get(self.campos[0])) #Procura  objeto pelo ID
        if obj is None:
            return jsonify({'update':0})
        else:
            # Usa programação reflexiva para alterar cada campo do objeto que foi alterado
            for c in self.campos:
                if request.args.get(c) is not None:
                    exec('obj.{} =request.args.get("{}")'.format(c, c))
                    dadosClasse.update()
                    return jsonify({'update':obj.COD})
    # Apaga um registro de classe
    def delete(self):
        #Procura pelo ID
        id=request.args.get(self.campos[0])
        obj = dadosClasse.readByID(id)
        if obj is None:
            return jsonify({"delete":0})
        else:
            dadosClasse.delete(obj)
            return jsonify({"delete":id})
#######################################
class AnotacaoRest(Resource):
    def __init__(self):
        self.campos=['COD','COD_CLASSE','CENTRO_X','CENTRO_Y','LARGURA','ALTURA','CONFIANCA',
                     'ERRADA','COD_IMAGEM']
    def get(self):
        if request.args.get(self.campos[0]) is not None:
            id_anotacao=request.args.get(self.campos[0])
            obj=dadosAnotacao.readByID(id_anotacao)
            schema=anotacaoSchema()
            anot=schema.dump(obj)
            # Aqui podemos fazer algumas alteracoes no dicionario para mostrar outras coisas
            anot['CLASSE']=obj.classe.CLASSE #Coloca o nome no lugar do COD
            #anot['IMAGEM']=None #Eu poderia retornar a imagem, mas isso iria lotar a API de info e gastar muita banda
            return jsonify(anot)
        # Acrescentar campos para pesquisa
        elif request.args.get(self.campos[1]) is not None:
            pass
        else:
            lista=dadosAnotacao.readAll()
            schema=anotacaoSchema(many=True)
            return jsonify(schema.dump(lista))
    def put(self):
        obj = dadosAnotacao.readByID(request.args.get(self.campos[0])) #Procura  objeto pelo ID
        if obj is None:
            return jsonify({'update':0})
        else:
            # Usa programação reflexiva para alterar cada campo do objeto que foi alterado
            for c in self.campos:
                if request.args.get(c) is not None:
                    exec('obj.{} =request.args.get("{}")'.format(c, c))
                    dadosAnotacao.update()
                    return jsonify({'update':obj.COD})
    def post(self):
        obj=dadosAnotacao.anotacao() # cria um objeto do tipo classe
        # Para cada campo de anotacao executa essa linha
        for c in self.campos:
            if c!='COD':
                exec("obj.{}=request.args.get('{}')".format(c,c))

        dadosClasse.create(obj)
        return jsonify({'insert':obj.COD})
    def delete(self):
        #Procura pelo ID
        id=request.args.get(self.campos[0])
        obj = dadosAnotacao.readByID(id)
        if obj is None:
            return jsonify({"delete":0})
        else:
            dadosAnotacao.delete(obj)
            return jsonify({"delete":id})
