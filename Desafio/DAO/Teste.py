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
testeLer()
testeNovo()
print("----------------------------------")
testeLer()