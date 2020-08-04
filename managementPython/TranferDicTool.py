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
    def openDicFile(self, data):
        resultDict = {"result": "", "error": 0, "message" : "",  "file" : None }
        word = data['word']
        generic = data['generics']
        domain = data['domains'][0:3]  # POS = 3 characters
        errorMSG = ""
        POS = ""
        # generic is none  pos is domain, else pos is generic

        if len(word) == 0:
            resultDict['error'] = 1
            resultDict["message"] += "No Word Specified !!!"
            return resultDict

        if len(generic) == 0:
            POS = domain
        else:
            POS = generic

        if len(POS) == 0:
            resultDict['error'] = 1
            resultDict["message"] += "No POS specified !!!"
            return resultDict

        newDomainPOS = ""
        # general DIC: nn, vb, ...
        # domain DIC: sPos == sNewPos

        if POS not in self.CONVERT_POS:
            newDomainPOS = POS
        else:
            newDomainPOS = self.CONVERT_POS[POS]

        firstLetter = word[0].lower()

        # make dictionary file name in KS DIC folder
        folderName = ""
        if POS not in self.FOLDER_Name:
            folderName = "General"
        else:
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

        relativePath = "\\DicMaTool_Web\\managementPython\\EXE\\"
        # when KS Dic file doesn't exist, generate file from N Dic file
        if not os.path.isfile(relativePath + KSDicFullFileName):
            self.generateKSDicFile(folderName, fileName)
            errorMSG = folderName + "\\" + fileName + " is generated !!!\n"
            resultDict["message"] = errorMSG
            # Print file generated massageBox

        if not os.path.isfile(relativePath + KSDicFullFileName):
            # print(KSDicFullFileName + " doesn't exist")
            errorMSG = KSDicFullFileName + " doesn't exist"
            resultDict['error'] = 1
            resultDict["message"] += errorMSG
            return resultDict
            # process end
        resultDict['file'] = open(relativePath + KSDicFullFileName)
        return resultDict


    def Search(self, data):
        word = data['word']

        key = "\"" + word + "\""

        resultDict = self.openDicFile(data)
        resultDict.update({ "foundLine" : 0 , "nextEntryLine" : 0 })
        if resultDict['error'] == 1 :
            return resultDict
        # print(allReadLines)

        allLines = resultDict['file'].readlines()
        index = 0
        #Is key in the list?
        if key+"\n" in allLines:
            index = allLines.index(key+"\n")
        else:
            # print(word + " is not in dictionary")
            errorMSG = word + " is not in dictionary"
            resultDict["error"] = 1
            resultDict["message"] = errorMSG
            return resultDict
        resultDict['foundLine'] = index

        # get key's means
        resultDict['result'] = allLines[index]

        length = 0
        for reads in allLines[index+1:] :
            if(reads[0] == '"'):
                break
            else :
                resultDict['result'] += reads
                length += 1
        resultDict['nextEntryLine'] = length + 1

        return resultDict


    def Update(self, replaceData):
        searchResult = self.Search({"result" : "", "errors" : ""})

        # file offset reset
        searchResult['file'].seek(0)
        allLines = searchResult['file'].readlines()
        updateData = []

        #수정 전의 부분
        updateData += allLines[: searchResult['foundLine'] - 1]
        #수정 부분
        for item in replaceData['updateText'].split("\n") :
            updateData.append(item + "\n") # split 과정중 사라진 \n을 붙여줌
        #수정 이후 부분
        updateData += allLines[searchResult['foundLine'] + searchResult['nextEntryLine']:]

        


        return replaceData



    def makeGenericDB(self):
        resultDict = {"result" : "", "errors" : 0}

        relativePath = "\\DicMaTool_Web\\managementPython\\EXE\\"
        fileName = "makeTransDicDB.exe"
        location = os.getcwd()
        os.chdir(relativePath)
        result = subprocess.run([relativePath + fileName], capture_output= True)
        output = result.stdout.decode('utf-8')
        os.chdir(location)

        if "DB open error!" in output:
            resultDict['result'] = "Make Generic DB Error"
            resultDict['error'] = 1
            return resultDict

        resultDict['result'] = "Make Generic DB Complete"
        return resultDict



    def makeDomainDB(self, word, genericPOS, domainPOS):
        print("transferMakeDomainDB")

    def generateKSDicFile(self, folderName, fileName):
        alterFullFileName = self.N_DIC_FOLDER + "\\" + folderName + "\\" + fileName
        relativePath = "\\DicMaTool_Web\\managementPython\\EXE\\"
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
    # testClass.makeGenericDB()
    testData = {'word': 'test', 'generics': 'noun', 'domains': 'atm (atomic)'}
    # testClass.Search(testData)
    testClass.Update(testData)

