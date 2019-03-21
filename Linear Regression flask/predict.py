from flask import Flask, request ,render_template
from flask import jsonify
from flask import json
import pandas as pd
from sklearn import linear_model
import statsmodels.api as sm

app = Flask(__name__) 

def time_to_minutes(time_str):  
    try:  
        hours, minutes, seconds = time_str.split(':')  
    except ValueError:  
        return -1  
    return int(hours)*60 + int(minutes) + int(seconds)/60.0  

def minutes_to_time(minutes):
    m=(int)(minutes%100)
    sec=(int)((minutes-m)*60)
    h=0	
    return'{:02d}:{:02d}:{:02d}'.format(h,m,sec)


@app.route('/',methods = ['GET','POST'])
def home():
    if request.method == 'GET':	
		nage1 = int(request.args['age'])
		ngen = (request.args['gen'])
		nchron = (request.args['chron'])
		nchar = (request.args['char'])
		ndoc_experience1 = int(request.args['docexp'])

		if ngen == 'male':
			ngen1 = 0
		else:
			ngen1 = 1
		
		if nchar == 'mostly_physical':
			nchar1 = 0
		elif nchar == 'half_physical_psychological':
			nchar1 = 1
		else:
			nchar1 = 2

		if  nchron == 'yes':
			nchron1 = 1
		else:
			nchron1 = 0 		
	
		
		data = pd.read_csv(r'dataset.csv')	  
		df=pd.DataFrame(data,columns=['Age','Gender','Consultation_time','Chronic_condition','Character_of_problem','Doctor_experience'])
		data.Gender[data.Gender == 'male'] = 0
		data.Gender[data.Gender == 'female'] = 1
		

		data.Chronic_condition[data.Chronic_condition == 'no'] = 0
		data.Chronic_condition[data.Chronic_condition == 'yes'] = 1
		

		data.Character_of_problem[data.Character_of_problem == 'mostly_physical'] = 0
		data.Character_of_problem[data.Character_of_problem == 'half_physical_psychological']= 1
		data.Character_of_problem[data.Character_of_problem == 'mostly_psychological']= 2
		


		X = df[['Age','Gender','Chronic_condition','Character_of_problem','Doctor_experience']] 

		Y = df['Consultation_time']

		i=0

		for y in Y:
			Y[i]=time_to_minutes(Y[i])
			i=i+1

	
		regr = linear_model.LinearRegression()
		regr.fit(X, Y)

		x=regr.predict([[nage1,ngen1,nchron1,nchar1,ndoc_experience1]])
		prediction=minutes_to_time(x)		
		response = app.response_class(response=json.dumps(prediction),status=200,mimetype='application/json')
		return response
		

if __name__ == '__main__':
    app.debug = True
    app.run(host ='0.0.0.0',port=5000)
