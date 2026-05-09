from flask import Flask, jsonify, render_template
from flask_cors import CORS
import json

app = Flask(__name__)
CORS(app)

with open('data.json', 'r') as file:
    data = json.load(file)

# Home page
@app.route('/')
def home():
    return render_template('index.html')


# Search using pincode
@app.route('/search/pincode/<code>')
def search_pincode(code):

    for item in data:
        if str(item["pincode"]) == str(code):
            return jsonify(item)

    return jsonify({"message": "No area found"})


# Search using area name
@app.route('/search/area/<name>')
def search_area(name):

    for item in data:
        if item["area"].lower() == name.lower():
            return jsonify(item)

    return jsonify({"message": "No pincode found"})


if __name__ == '__main__':
    app.run(debug=True)