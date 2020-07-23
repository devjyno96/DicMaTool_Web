class transferDic :
    def __init__(self):
        print("init")


    def Search(self, data):
        print(data['word'] + " : " + data['generics'] + " : " + data['domains'])


    def Update(self, word, genericPOS, domainPOS):
        print("transferDicUpdate")

    def makeGenericDB(self, word, genericPOS, domainPOS):
        print("transferMakeGenericDB")


    def makeDomainDB(self, word, genericPOS, domainPOS):
        print("transferMakeDomainDB")

