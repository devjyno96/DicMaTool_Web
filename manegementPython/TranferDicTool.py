class transferDic :
    KS_DIC_FOLDER = "KS-DICT"
    N_DIC_FOLDER = "N-DICT"
    CONVERT_POS = {
        "noun": "nn",
        "verb": "vb",
        "adj": "adj",
        "adv": "adv",
        "pron": "prn",
        "conj": "cnj",
        "prep": "prp"
    }
    FOLDER_Name = {
            "nar" : "Airplane",
            "arc" : "Architecture",
            "atm" : "Atomic",
            "ato" : "Auto",
            "bio" : "Bio",
            "jco" : "Computer-J",
            "nco" : "Computer-N",
            "nee" : "Economy-N",
            "vee" : "Economy-V",
            "ind" : "Industry",
            "med" : "Medical",
            "tac" : "Military",
            "pat" : "Patent",
            "npo" : "Politics",
            "shp" : "Ship",
            "nsp" : "Sports-N",
            "vsp" : "Sports-V",
            "tel" : "Telecom"
        }

    def __init__(self):
        print("init")


    def Search(self, data):
        word = data['word']
        generic = data['generics']
        domain = data['domains'][0:3]
        POS = ""
        # generic is none  pos is domain, else pos is generic
        if len(generic) == 0 :
            POS = domain
        else :
            POS = generic

        newDomainPOS = ""

        if POS not in self.CONVERT_POS :
            newDomainPOS = POS
        else :
            newDomainPOS = self.CONVERT_POS[POS]

        firstLetter = word[0].lower()

        folderName = ""
        if POS not in self.FOLDER_Name :
            folderName = "General"
        else :
            folderName = self.FOLDER_Name[POS]

        KSDicFullFileName = self.KS_DIC_FOLDER + "\\" + folderName + "\\"
        NDicFullFileName = self.N_DIC_FOLDER + "\\" + folderName + "\\"
        fileName = "dic"
        if newDomainPOS not in ['pron', 'prep', 'conj']:
            fileName += firstLetter
        fileName += '.'
        fileName += newDomainPOS
        NDicFullFileName += fileName
        KSDicFullFileName += fileName
        KSDicFullFileName += '.txt'
        print(NDicFullFileName)
        print(KSDicFullFileName)


    def Update(self, word, genericPOS, domainPOS):
        print("transferDicUpdate")

    def makeGenericDB(self, word, genericPOS, domainPOS):
        print("transferMakeGenericDB")


    def makeDomainDB(self, word, genericPOS, domainPOS):
        print("transferMakeDomainDB")

    def generateKSDicFile(self, folderName, fileName):
        alterFullFileName = self.N_DIC_FOLDER + "\\" + folderName + "\\" + fileName
        cnExe = "EXE\\cn.exe"
        cnArgument = "-nc " + alterFullFileName +  " " + fileName + ".jh"
        # process run cn.exe (argument is cnArgument)

        ksExe = "EXE\\kscode.exe"
        ksArgument = "-jk " + fileName + ".jh" + self.KS_DIC_FOLDER + "\\" + folderName + "\\" + fileName +'.txt'
        # process run kscode.exe (argument is ksArgument)


        print("generateKsDicFile")

if __name__ == "__main__" :
    testClass = transferDic()
    testData = {'word': 'test', 'generics': '', 'domains': 'atm (atomic)'}
    testClass.Search(testData)