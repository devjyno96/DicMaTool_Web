from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
import json
from managementPython import TranferDicTool

app = Flask(__name__)
app.testing = True

transfer = TranferDicTool.transferDic()


@app.route('/')
def viewIndex():
    return render_template('trans.html')

@app.route('/trans')
def viewTrans():
    return render_template('trans.html')

@app.route('/lex')
def viewLex():
    return render_template('lex.html')


@app.route('/postSearch', methods=['POST'])
def postSearch():
    search = request.get_json()  # json 데이터를 받아옴
    result = transfer.Search(search)
    del result['file']
    return jsonify(result)  # 받아온 데이터를 다시 전송


@app.route('/postUpdate', methods=['POST'])
def postUpdate():
    update = request.get_json()  # json 데이터를 받아옴
    result = transfer.Update(update)
    # del result['file']
    return jsonify(result)  # 받아온 데이터를 다시 전송


@app.route('/postMakeGenericDB', methods=['POST'])
def postMakeGenericDB():
    result = transfer.makeGenericDB()
    return jsonify(result)  # 받아온 데이터를 다시 전송


@app.route('/postMakeDomainDB', methods=['POST'])
def postMakeDomainDB():
    data = request.get_json()  # json 데이터를 받아옴
    result = transfer.makeDomainDB(data)
    return jsonify(result)  # 받아온 데이터를 다시 전송


@app.route('/getJson', methods=['get'])
def getJson():
    user = {
        "test": "testGetJson"
    }
    return jsonify(user)  # 받아온 데이터를 다시 전송


if __name__ == "__main__":
    app.run()
