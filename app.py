from flask import Flask, request
from model import generateAI
import pickle

generateAI()
ai=pickle.load(open('ai.pkl','rb'))
app=Flask(__name__)

@app.route('/')
def homepage():
    return "Server Running"

@app.route('/predict')#/predict?ir=0
def predict():
    ir=request.args.get('ir')
    ir=int(ir)
    data=[[ir]]
    result=ai.predict(data)[0]#['object']
    return result

if(__name__)=="_main_":
    app.run(host='0.0.0.0',port=3000)