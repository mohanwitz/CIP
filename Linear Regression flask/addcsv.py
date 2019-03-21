from flask import Flask, request ,render_template
from flask import jsonify
from flask import json
import pandas as pd
import matplotlib.pyplot as plt

app = Flask(__name__) 

@app.route('/',methods = ['GET','POST'])
def home():
     if request.method == 'GET':             
        nage = (request.args['age'])
        ngen = (request.args['gen'])
        ntime = request.args['time']
        nchron = (request.args['chron'])		 
        nchar = (request.args['char'])
        ndoc_experience = (request.args['docexp'])
        if nage == 'null':
            return str('not inserted')
        data = pd.read_csv(r'dataset.csv')
        df = pd.DataFrame(data,columns=['Age','Gender','Consultation_time','Chronic_condition','Character_of_problem','Doctor_experience'])

        df2 = pd.DataFrame([[nage,ngen,ntime,nchron,nchar,ndoc_experience]],columns=['Age','Gender','Consultation_time','Chronic_condition','Character_of_problem','Doctor_experience'])
        
        df3 = df.append(df2,ignore_index=True)        
        
        df3.to_csv("dataset.csv", index=False)
        return str('Inserted Successfully')              

if __name__ == '__main__':
    app.debug = True
    app.run(host ='0.0.0.0',port=5005) 

    #http://10.10.74.156:5005/?age=80&gen=1&chron=1&con=4&char=2&docexp=16&time=10