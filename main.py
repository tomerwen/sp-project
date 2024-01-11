from flask import Flask, render_template, request, jsonify
from pymongo import MongoClient
client = MongoClient('mongodb://root:example@mongodb:27017/userdata')
db = client['userdata']
collection = db['users']

app = Flask(__name__)

@app.route("/")
def landing_page():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    user_data = {
        'name': request.form.get('name'),
        'email': request.form.get('email'),
        'company': request.form.get('company')
    }
    
    collection.insert_one(user_data)


    return render_template("submitted.html")

if __name__ == '__main__':
    app.run(debug=True)