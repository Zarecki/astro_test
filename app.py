from flask import Flask 
import requests
import json


app = Flask(__name__)

def fetch():
    response = requests.get('https://data.nasa.gov/resource/gvk9-iz74.json')
    data = response.text
    jsonified = json.loads(data)
    print(len(jsonified))
    return jsonified

# if __name__ == '__main__':
#     app.run(debug=True)