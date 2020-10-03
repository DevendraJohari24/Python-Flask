from flask import Flask, jsonify, request
from flask_restful import Api,Resource

from pymongo import MongoClient

app = Flask(__name__)
api = Api(app)

client = MongoClient("mongodb://db:27017")
db = client.aNewDB
UserNum = db["UserNum"]

UserNum.insert({
    'num_of_users':0
})

class Visit(Resource):
    def get(self):
        prev_num = UserNum.find({})[0]['num_of_users']
        new_num = prev_num + 1
        UserNum.update({}, {"$set":{"num_of_users":new_num}})
        return str("Hello user " + str(new_num))


def checkPostedData(postedData , funcName):
    if ((funcName == "add") or (funcName == "substract") or (funcName == "multiply")):
        if "x" not in postedData or "y" not in postedData:
            return 301
        else:
            return 200
    elif (funcName == "division"):
        if "x" not in postedData or "y" not in postedData:
            return 301
        elif int(postedData["y"])==0:
            return 302
        else:
            return 200

class Add(Resource):
    def post(self):
        #Step1: Get Posted Data
        postedData = request.get_json()
        #Step 1b : Verify Validity of posted data
        status_code = checkPostedData(postedData, "add")
        if(status_code!=200):
            retJson = {
                "Message": "An error happened",
                "Status Code": status_code
            }
            return jsonify(retJson)

        x = postedData["x"]
        y = postedData["y"]
        x = int(x)
        y = int(y)

        # Step2 : Add the posted Data
        ret = x+y
        retMap = {
            'Message': ret,
            'Status Code': 200
        }
        return jsonify(retMap)

class Substract(Resource):
    def post(self):
        #Step1: Get Posted Data
        postedData = request.get_json()
        #Step 1b : Verify Validity of posted data
        status_code = checkPostedData(postedData, "substract")
        if(status_code!=200):
            retJson = {
                "Message": "An error happened",
                "Status Code": status_code
            }
            return jsonify(retJson)

        x = postedData["x"]
        y = postedData["y"]
        x = int(x)
        y = int(y)

        # Step2 : Add the posted Data
        ret = x-y
        retMap = {
            'Message': ret,
            'Status Code': 200
        }
        return jsonify(retMap)


class Multiply(Resource):
    def post(self):
        #Step1: Get Posted Data
        postedData = request.get_json()
        #Step 1b : Verify Validity of posted data
        status_code = checkPostedData(postedData, "multiply")
        if(status_code!=200):
            retJson = {
                "Message": "An error happened",
                "Status Code": status_code
            }
            return jsonify(retJson)

        x = postedData["x"]
        y = postedData["y"]
        x = int(x)
        y = int(y)

        # Step2 : Add the posted Data
        ret = x*y
        retMap = {
            'Message': ret,
            'Status Code': 200
        }
        return jsonify(retMap)



class Division(Resource):
    def post(self):
        #Step1: Get Posted Data
        postedData = request.get_json()
        #Step 1b : Verify Validity of posted data
        status_code = checkPostedData(postedData, "division")
        if(status_code!=200):
            retJson = {
                "Message": "An error happened",
                "Status Code": status_code
            }
            return jsonify(retJson)

        x = postedData["x"]
        y = postedData["y"]
        x = int(x)
        y = int(y)

        # Step2 : Add the posted Data
        ret = (x*1.0)/y
        retMap = {
            'Message': ret,
            'Status Code': 200
        }
        return jsonify(retMap)

api.add_resource(Add, "/add")
api.add_resource(Substract, "/substract")
api.add_resource(Multiply, "/multiply")
api.add_resource(Division, "/division")
api.add_resource(Visit, "/hello")

@app.route('/')
def hello_world():
    return "Hello World!"












    

if __name__=="__main__":
    app.run(host='0.0.0.0')
    
    
    
    
    
    
    
    
    
    
    
