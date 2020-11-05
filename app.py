from flask import Flask, render_template, request
import jsonify
import requests
import pickle
import numpy as np
import pandas as pd
import sklearn  #here sklearn=0.22 version is installed. v0.31 gives error
app = Flask(__name__)

#make sure you have installed gunicorn in this env

#loading pickle files
model = pickle.load(open('cos_sim.pkl', 'rb'))

@app.route('/',methods=['GET'])
def Home():
    return render_template('index.html')



@app.route("/predict", methods=['POST'])
def predict():
    
    if request.method == 'POST':
        
        Dish_Name = request.form['Dish_Name']
        d = pd.DataFrame({'Dish_Name':[Dish_Name]})
        
 prediction = model1[Dish_Name]
        output= prediction


if __name__=="__main__":
    app.run(debug=True)