from flask import Flask
from flask_restful import Api
import rest

# Instancia o aplicativo como um objeto
app=Flask(__name__)
api=Api(app)

# Configura os caminhos para cada recurso
api.add_resource(rest.ClasseRest,'/ClasseObjetos',endpoint='classes')
api.add_resource(rest.AnotacaoRest,'/Anotacoes',endpoint='anotacoes ')



if __name__=="__main__":
    app.run(debug=True)