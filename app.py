from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
import json
app = Flask(__name__)
app.testing = True

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/postSearch', methods = ['POST'])
def postSearch():
    search = request.get_json() #json 데이터를 받아옴
    searchResult = {'dicInfoLeft' : 'left','dicInfoRight' : 'right'}
    return jsonify(searchResult) # 받아온 데이터를 다시 전송


@app.route('/getJson', methods = ['get'])
def getJson():
    user = {
        "test" : "testGetJson"
    }
    return jsonify(user)# 받아온 데이터를 다시 전송


if __name__ == "__main__":
    app.run()
