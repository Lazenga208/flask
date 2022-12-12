import json
from flask import Flask,request

app = Flask(__name__)

with open('capsules.json', 'r') as f:
    data = json.load(f)

def sameProfile(capsules,profile):
    for p in profile:
        if capsules[p]!=profile[p]:
            return False
    return True
# GET
@app.route("/capsules/all")
def returnAll():
    return str(data)

@app.route('/capsules/byName/<name>')
def returnByName(name):
       for d in data:
           if d['name']==name:
               return d
           return "no such name"

@app.route('/capsules/byId/<id>')
def returnById(id):
       for d in data:
           if str(d['id'])==id:
               return d
       return "no such id"

@app.route('/image/<id>')
def returnByImageId(id):
       for d in data:
           if str(d['image'])==id:
               return d
       return "no such image id"

# POST
@app.route('/filterByProfile', methods=['POST'])
def byProfile():
    profile=request.json['profile']
    answer=[]
    for d in data:
        if sameProfile(d['profile'],profile)==True:
            answer.append(d)
    return str(answer)

# PUT
@app.route('/capsules/id',methods=['PUT'])
def put():
    for d in data:
        id=request.json
        if d['id']==id['id']:
            d['price']+=10
            with open("capsules.json", "w") as jsonFile:
                json.dump(data, jsonFile)
    return id

if __name__ == '__main__':
    app.run()