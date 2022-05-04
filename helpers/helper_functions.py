import requests
import json

def fetch():
    response = requests.get('https://data.nasa.gov/resource/gvk9-iz74.json')
    data = response.text
    jsonified = json.loads(data)
    return jsonified
