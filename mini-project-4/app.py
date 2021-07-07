import numpy as np
import pandas as pd
from flask import Flask, render_template, request
import pickle


app = Flask(__name__)
model = pickle.load(open("testmodel.p", "rb"))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
    test = request.form.get('total_income', type=float)
    return render_template("index.html", prediction_text= 'Answer: {}'.format(test))

if __name__ == '__main__':
    app.debug = True
    app.run()