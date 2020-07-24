import subprocess
import os


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

    """
    def __init__(self):
        print("init")
    """


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


        self.generateKSDicFile(folderName, fileName)


    def Update(self, word, genericPOS, domainPOS):
        print("transferDicUpdate")

    def makeGenericDB(self, word, genericPOS, domainPOS):
        print("transferMakeGenericDB")


    def makeDomainDB(self, word, genericPOS, domainPOS):
        print("transferMakeDomainDB")

    def generateKSDicFile(self, folderName, fileName):
        alterFullFileName = self.N_DIC_FOLDER + "\\" + folderName + "\\" + fileName
        relativePath = "\\DicMaTool_Web\\manegementPython\\EXE\\"
        # cnExe = "EXE\\cn.exe"
        cnExe = "cn.exe"
        # cnArgument = "-nc " + alterFullFileName +  " " + fileName + ".jh"
        # process run cn.exe (argument is cnArgument)
        subprocess.run([ relativePath + cnExe, "-nc", relativePath + alterFullFileName,  relativePath+ fileName + ".jh"])

        # ksExe = "EXE\\kscode.exe"
        ksExe = "kscode.exe"
        # ksArgument = "-jk " + fileName + ".jh" + self.KS_DIC_FOLDER + "\\" + folderName + "\\" + fileName + '.txt'
        # process run kscode.exe (argument is ksArgument)
        subprocess.run([relativePath + ksExe, "-jk", relativePath + fileName + ".jh", relativePath + self.KS_DIC_FOLDER + "\\" + folderName + "\\" + fileName + '.txt'])

        # FILE delete fileName+".jh"
        removeFileName = relativePath + fileName + ".jh"
        if os.path.isfile(removeFileName) :
            os.remove(removeFileName)


if __name__ == "__main__" :
    testClass = transferDic()
    testData = {'word': 'test', 'generics': '', 'domains': 'atm (atomic)'}
    testClass.Search(testData)

