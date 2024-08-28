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
testeLer()
