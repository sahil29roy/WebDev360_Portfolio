from flask import Flask, render_template
from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017")
db = client['portfolio']
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/contactus', methos=['POST'])
def contatus():
    name= request.form['name']
    email=request.form['email']
    message=request.form['message']

    doc = {
        'name' : name,
        'email' : email,
        'message' : message
    }

    db.contactus.insert_one(doc)
    return "Thank for contacting us!!"
app.run(port=80)