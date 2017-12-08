from flask import Flask
from flask import jsonify
from flask import request
from flask import Response
from flask import render_template
import simplejson as json


app = Flask(__name__)



with open('restodb.json') as json_data:
    inp = json.load(json_data)
    restaurant_list = []
    for data in inp['restoDB']:
        print (data)
        restaurant_list.append(data)


@app.route('/')
def restoHome():
	return render_template("index.html")
	

@app.route('/restodb/allrestaurants',methods=['GET'])
def getAllResto():
    return render_template("index.html", items=restaurant_list)

@app.route('/restodb/allrestaurants/<ratings>',methods=['GET'])
def getResto(ratings):
	rst = [ rest for rest in restaurant_list if (rest['ratings'] == ratings) ]
	return render_template("index.html", items=rst)



@app.route('/restodb/allrestaurants/jsondata',methods=['GET'])
def getAllRestoJson():
    return jsonify({'restoDB':restaurant_list})

@app.route('/restodb/allrestaurants/jsondata/<ratings>',methods=['GET'])
def getRestoJson(ratings):
	rst = [ rest for rest in restaurant_list if (rest['ratings'] == ratings) ] 
	return jsonify({'rest':rst})

if __name__ == '__main__':
 app.run(host='0.0.0.0')