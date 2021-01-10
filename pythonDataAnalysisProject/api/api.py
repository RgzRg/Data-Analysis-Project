from flask import Flask, request, redirect, url_for, flash, jsonify
import numpy as np
import pickle as p
import json
import os


app = Flask(__name__)


@app.route('/api/', methods=['POST'])
def makecalc():
    data = request.get_json(force=True)
    finalData = []
    datas = []
    for value in data.values():
        datas.append(value)
    finalData.append(datas)
    prediction = model.predict(finalData)
    print("Resullt : " + str(prediction[0]))
    return jsonify(int(prediction[0]))
    
    

if __name__ == '__main__':
    
    model = p.load(open("../model.pickle", 'rb'))
    app.run(debug=True, host='127.0.0.1')