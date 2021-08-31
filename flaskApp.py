from flask import Flask,jsonify, request

app = Flask(__name__) 

contacts = [
    {
        'id': 1,
        'title': u'Provide Contact',
        'description': u'Amitava,Adrish,Priyanshu', 
        'done': False
    },
    {
        'id': 2,
        'title': u'Learn Python',
        'description': u'Need to find a good Python tutorial on the web', 
        'done': False
    }
]

@app.route("/add-data",methods=["POST"])

def add_task():
    if not request.json:
        return jsonify({
            "status":"error"
            "message":"Please provide the data!"
        },400)
        