import orm

daoClasse=orm.CLASSE()

def testeLer():
    classes=daoClasse.readAll()
    for c in classes:
        print(str(c.COD)+" classe: "+c.CLASSE)

def testeNovo():
    novaClasse=daoClasse.classe()

    novaClasse.CLASSE='Scooter'
    daoClasse.create(novaClasse)
def testeReadByID():
    classe=daoClasse.readByID(6)
    print("Lendo um único registro")
    print("COD: "+str(classe.COD)+" NOME: "+classe.CLASSE)
def testeAlterar():
    print("Alterando o registro")
    classe=daoClasse.readByID(8)
    classe.CLASSE='Carroça' # Palavra a ser alterada
    daoClasse.update()
def testeExcluir():
    print("Teste função excluir")
    classe=daoClasse.readByID(8)
    daoClasse.delete(classe)
testeLer()
#testeNovo()
#testeReadByID()
#testeAlterar()
#testeExcluir()
#testeLer()

"""
    Vou performar uma alteração, para concentrar os testes todos juntos
"""
class Teste:
    def testeLer(self):
        pass
    def testeNovo(self):
        pass
    def testeLerUnico(self):
        pass
    def testeAlterar(self):
        pass
    def testeExlcuir(self):
        pass
class TestaAnotacao(Teste):
    def __init__(self):
        self.daoAnotacao=orm.ANOTACAO()
    def testeLer(self):
        anotacoes=self.daoAnotacao.readAll()
        for c in anotacoes:
            print("COD: "+str(c.COD)+" COD_CLASSE:"+str(c.COD_CLASSE)+" CENTRO("+str(c.CENTRO_X)+
                  ";"+str(c.CENTRO_Y)+") confiança: "+str(c.CONFIANCA))

    def testeNovo(self):
        print("Insere uma nova anotação")
        novaAnotacao = self.daoAnotacao.anotacao()

        novaAnotacao.COD_CLASSE = 7
        novaAnotacao.CENTRO_X = 123
        novaAnotacao.CENTRO_Y = 356
        novaAnotacao.LARGURA=12
        novaAnotacao.ALTURA=90
        novaAnotacao.CONFIANCA=0.72
        novaAnotacao.ERRADA=False
        novaAnotacao.COD_IMAGEM=None


        self.daoAnotacao.create(novaAnotacao)

    def testeLerUnico(self):
        anotacao = self.daoAnotacao.readByID(6)
        print("Lendo um único registro")
        print("COD: " + str(anotacao.COD) + " confianca: " + str(anotacao.CONFIANCA))

    def testeAlterar(self):
        print("Alterando o registro de anotacao")
        anotacao= self.daoAnotacao.readByID(8)
        anotacao.CENTRO_X = 456  # Palavra a ser alterada
        anotacao.CENTRO_Y= 789
        daoClasse.update()

    def testeExcluir(self):
        print("Teste função excluir")
        anotacao = self.daoAnotacao.delete()
        self.daoAnotacao.delete(anotacao)
testadorAnotacao=TestaAnotacao()
testadorAnotacao.testeLer()
testadorAnotacao.testeNovo()
testadorAnotacao.testeLer()