from flask import Flask, request ,render_template
from flask import jsonify
from flask import json

doc1003 = dict()
app = Flask(__name__) 


@app.route('/',methods = ['GET','POST'])
def home():
    if request.method == 'GET':   
        did = (request.args['did'])
        time = (request.args['time'])
        tokeno = (request.args['tokeno'])
        date = (request.args['date'])
        distance = (request.args['distance'])
        duration = (request.args['duration'])
        pid = (request.args['pid'])
        lat = (request.args['lat'])
        lon = (request.args['long'])

        temp = {'time':time,'distance':distance,'duration':duration,'pid':pid,'lat':lat,'long':lon+' '}
        if did == '1003':
            doc1003[tokeno] = temp

        f=open("test2.txt", "a+")
        f.write(did)
        f.write(",")
        f.write(time)
        f.write(",")
        f.write(tokeno)
        f.write(",")
        f.write(date)
        f.write(",")
        f.write(distance)
        f.write(",")
        f.write(duration)
        f.write(",")
        f.write(pid)
        f.write("\n")
       # f.write(",")
       # f.write(lat)
       ## f.write(",")
       # f.write(lon)
       # f.write("\n")
        f.close()
        return ""

@app.route('/test')
def index():
    print doc1003

if __name__ == '__main__':
    app.debug = True
    app.run(host ='0.0.0.0',port=5020)
