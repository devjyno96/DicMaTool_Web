import subprocess
import os


class lexicalDic:
    KS_DIC_FOLDER = "KS-DICT"
    N_DIC_FOLDER = "N-DICT"

    LEX_DIC = "LEX-DIC\\base.dic"
    LEX_PROB_DIC = "LEX-DIC\\lpf.lst"
    RELATIVE_PATH = "\\DicMaTool_Web\\managementPython\\EXE\\"

    def makeLexicalDB(self):
        resultDict = {"result": "", "error": 0}

        fileName = "makeTransDicDB.exe"
        location = os.getcwd()
        os.chdir(self.RELATIVE_PATH)
        result = subprocess.run([self.RELATIVE_PATH + fileName], capture_output=True)
        output = result.stdout.decode('utf-8')
        os.chdir(location)

        if "DB open error!" in output:
            resultDict['result'] = "Make Lexical DB Error"
            resultDict['error'] = 1
            return resultDict

        resultDict['result'] = "Lexical Dictionary DB is created !"
        return resultDict


    def makeProbDB(self):
        resultDict = {"result": "", "error": 0}

        fileName = "makeLexProbDicDB.exe"
        location = os.getcwd()
        os.chdir(self.RELATIVE_PATH)
        result = subprocess.run([self.RELATIVE_PATH + fileName], capture_output=True)
        output = result.stdout.decode('utf-8')
        os.chdir(location)

        if "DB open error!" in output:
            resultDict['result'] = "Make Prob DB Error"
            resultDict['error'] = 1
            return resultDict

        resultDict['result'] = "Lexical Prob Dictionary DB is created !"
        return resultDict


    def lexFileSearch(self, data):
        resultDict = {"result": "", "error": 0, "message": "", "file": None}
        # generic is none  pos is domain, else pos is generic

        if not os.path.isfile(self.RELATIVE_PATH + self.LEX_DIC):
            resultDict['error'] = 1
            resultDict["message"] = self.LEX_DIC + " doesn't exist !!!"
            return resultDict
        resultDict['file'] = open(self.RELATIVE_PATH + self.LEX_DIC)
        return resultDict


    def lexSearch(self, data):
        resultDict = self.lexFileSearch(data)
        resultDict.update({"foundLine": 0})

        if resultDict['error'] == 1:
            return resultDict

        word = data['word']

        if len(word) == 0:
            resultDict['error'] = 1
            resultDict["message"] = "No Word Specified !!!"
            return resultDict

        allLines = resultDict['file'].readlines()
        keywordAllLines = [items.split(',')[0] for items in allLines] # keyword extraction

        if word in keywordAllLines :
            resultDict['foundLine'] = keywordAllLines.index(word)
            resultDict['result'] = allLines[resultDict['foundLine']]
        else :
            resultDict["error"] = 1
            resultDict["message"] = word + " is not in dictionary"
            return resultDict

        return resultDict


    def probFileSearch(self):
        resultDict = {"result": "", "error": 0, "message": "", "file": None}
        # generic is none  pos is domain, else pos is generic

        if not os.path.isfile(self.RELATIVE_PATH + self.LEX_PROB_DIC):
            resultDict['error'] = 1
            resultDict["message"] = self.LEX_PROB_DIC + " doesn't exist !!!"
            return resultDict
        resultDict['file'] = open(self.RELATIVE_PATH + self.LEX_PROB_DIC)
        return resultDict


    def probSearch(self, data):
        resultDict = self.probFileSearch()
        resultDict.update({"foundLine": 0})

        if resultDict['error'] == 1:
            return resultDict

        word = data['word']

        if len(word) == 0:
            resultDict['error'] = 1
            resultDict["message"] = "No Word Specified !!!"
            return resultDict

        allLines = resultDict['file'].readlines()
        keywordAllLines = [items.split(' ')[0] for items in allLines]  # keyword extraction

        if word in keywordAllLines:
            resultDict['foundLine'] = keywordAllLines.index(word)
            resultDict['result'] = allLines[resultDict['foundLine']]
        else:
            resultDict["error"] = 1
            resultDict["message"] = word + " is not in dictionary"
            return resultDict

        return resultDict


    def lexUpdate(self, data):
        searchResult = self.lexSearch(data)
        word = data['word']
        updateText = data['updateText']
        updateWord = updateText.split(',')[0]
        if searchResult['error'] == 1 :
            return searchResult

        if updateText == "" :
            searchResult['error'] = 1
            searchResult['message'] = "no new LEX content !!!"
            return searchResult

        if len(updateWord) < 0 :
            searchResult['error'] = 1
            searchResult['message'] = "ill formed LEX DIC entry !!!"
            return searchResult

        if updateWord[0:len(word)] != word :
            searchResult['error'] = 1
            searchResult['message'] = "update entry word is different from the given word !!!"
            return searchResult

        searchResult['file'].seek(0)
        allLines = searchResult['file'].readlines()
        keywordAllLines = [items.split(',')[0] for items in allLines] # keyword extraction

        index = -1

        for key in keywordAllLines :
            if updateWord <= key :
                index = keywordAllLines.index(key)
                break

        if index < 0 :
            return searchResult

        updateData = []

        updateData += allLines[ : index]


        updateData.append(updateText)
        if updateWord == keywordAllLines[index] :
            updateData += allLines[index + 1 : ] # 갱신작업을 한것 = index를 저장하지 않고 넘어감
        else :
            updateData.append(allLines[index])
            updateData += allLines[index + 1: ] # 추가한것 index 를 포함해 저장한다

        writeFile = open(self.RELATIVE_PATH + self.LEX_DIC, "w")
        writeFile.write("".join(updateData))

        searchResult['result'] = "LEX DIC is updated !!!"
        return searchResult


    def probUpdate(self, data):
        searchResult = self.probSearch(data)
        word = data['word']
        updateText = data['updateText']
        updateWord = updateText.split(' ')[0]
        if searchResult['error'] == 1:
            return searchResult

        if updateText == "":
            searchResult['error'] = 1
            searchResult['message'] = "no new Lex Prob content !!!"
            return searchResult

        if len(updateWord) < 0:
            searchResult['error'] = 1
            searchResult['message'] = "ill formed Lex Prob DIC entry !!!"
            return searchResult

        if updateWord[0:len(word)] != word:
            searchResult['error'] = 1
            searchResult['message'] = "update entry word is different from the given word !!!"
            return searchResult

        searchResult['file'].seek(0)
        allLines = searchResult['file'].readlines()
        keywordAllLines = [items.split(' ')[0] for items in allLines]  # keyword extraction

        index = -1

        for key in keywordAllLines:
            if updateWord <= key:
                index = keywordAllLines.index(key)
                break

        if index < 0:
            return searchResult

        updateData = []

        updateData += allLines[: index]

        updateData.append(updateText)
        if updateWord == keywordAllLines[index]:
            updateData += allLines[index + 1:]  # 갱신작업을 한것 = index를 저장하지 않고 넘어감
        else:
            updateData.append(allLines[index])
            updateData += allLines[index + 1:]  # 추가한것 index 를 포함해 저장한다

        writeFile = open(self.RELATIVE_PATH + self.LEX_PROB_DIC, "w")
        writeFile.write("".join(updateData))

        searchResult['result'] = "Lex Prob DIC is updated !!!"
        return searchResult

if __name__ == "__main__":
    testClass = lexicalDic()
    # testClass.makeGenericDB()
    testData = {'word': 'test'}
    print(testClass.probSearch(testData))
