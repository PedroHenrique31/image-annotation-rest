import orm

daoClasse=orm.CLASSE()

def testeLer():
    classes=daoClasse.readAll()
    for c in classes:
        print(str(c.COD)+" classe: "+c.CLASSE)
testeLer()