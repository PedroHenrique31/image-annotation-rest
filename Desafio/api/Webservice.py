from flask import Flask,request,send_file
#from flask_cors import CORS
from flask_restful import Api
import rest

app=Flask(__name__)
api=Api(app)

api.add_resource(rest.ClasseRest,'/ClasseObjetos',endpoint='classes')
api.add_resource(rest.AnotacaoRest,'/Anotacoes',endpoint='anotacoes ')



if __name__=="__main__":
    app.run(debug=True)