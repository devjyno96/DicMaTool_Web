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
        """

        :param data: word, generic, domains
        :type data: dict{str, str, str}
        :return: result
        :type return: dict{result : str, error: str}
        """
        resultDict = {"result" : "", "errors" : ""}
        word = data['word']
        generic = data['generics']
        domain = data['domains'][0:3] # POS = 3 characters
        errorMSG = ""
        POS = ""
        # generic is none  pos is domain, else pos is generic

        if len(word) == 0:
            errorMSG = "No Word Specified !!!"
            resultDict["errors"] = errorMSG
            return resultDict

        if len(generic) == 0 :
            POS = domain
        else :
            POS = generic

        if len(POS) == 0 :
            errorMSG = "No POS specified !!!"
            resultDict["errors"] = errorMSG
            return resultDict



        newDomainPOS = ""
        # general DIC: nn, vb, ...
        # domain DIC: sPos == sNewPos

        if POS not in self.CONVERT_POS :
            newDomainPOS = POS
        else :
            newDomainPOS = self.CONVERT_POS[POS]

        firstLetter = word[0].lower()


        # make dictionary file name in KS DIC folder
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

        relativePath = "\\DicMaTool_Web\\manegementPython\\EXE\\"
        # when KS Dic file doesn't exist, generate file from N Dic file
        if not os.path.isfile(relativePath + KSDicFullFileName):
            self.generateKSDicFile(folderName, fileName)
            errorMSG = folderName + "\\" + fileName + " is generated !!!\n"
            resultDict["errors"] = errorMSG
            # Print file generated massageBox

        if not os.path.isfile(relativePath + KSDicFullFileName):
            # print(KSDicFullFileName + " doesn't exist")
            errorMSG = KSDicFullFileName + " doesn't exist"
            resultDict["errors"] = errorMSG
            return resultDict
            # process end

        key = "\"" + word + "\""
        # ANSI is to need decoded by mbcs
        # allReadLines = open(relativePath + KSDicFullFileName, encoding="mbcs")
        allReadLines = open(relativePath + KSDicFullFileName)
        allLines = allReadLines.readlines()
        index = 0
        #Is key in the list?
        if key+"\n" in allLines:
            index = allLines.index(key+"\n")
        else:
            # print(word + " is not in dictionaly")
            errorMSG = word + " is not in dictionaly"
            resultDict["errors"] = errorMSG
            return resultDict
            # process end

        # get key's means
        result = allLines[index]
        for reads in allLines[index+1:] :
            if(reads[0] == '"'):
                break
            else :
                resultDict['result'] += reads

        return resultDict


    def Update(self, word, genericPOS, domainPOS):
        print("transferDicUpdate")

    def makeGenericDB(self):
        relativePath = "\\DicMaTool_Web\\manegementPython\\EXE\\"
        fileName = "makeTransDicDB.exe"
        # os.chdir(os.getcwd())
        subprocess.run([relativePath + fileName])



    def makeDomainDB(self, word, genericPOS, domainPOS):
        print("transferMakeDomainDB")

    def generateKSDicFile(self, folderName, fileName):
        alterFullFileName = self.N_DIC_FOLDER + "\\" + folderName + "\\" + fileName
        relativePath = "\\DicMaTool_Web\\manegementPython\\EXE\\"
        # cnExe = "EXE\\cn.exe"
        cnExe = "cn.exe"
        # cnArgument = "-nc " + alterFullFileName +  " " + fileName + ".jh"
        # process run cn.exe (argument is cnArgument)
        subprocess.run([relativePath + cnExe, "-nc", relativePath + alterFullFileName,  relativePath+ fileName + ".jh"])

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
    testClass.makeGenericDB()
    """
    testData = {'word': 'test', 'generics': 'noun', 'domains': 'atm (atomic)'}
    testClass.Search(testData)
    """

