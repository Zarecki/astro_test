import requests
import json
from flask import jsonify
from datetime import datetime
import repositories.facility_repository as facility_repository
from models.facility import Facility

# the fetch from the nasa endpoint
def fetch():
    response = requests.get('https://data.nasa.gov/resource/gvk9-iz74.json')
    data = response.text
    return json.loads(data)

# handling the saving of multiple new entries to the db
def save_multiple_entries(entries, initial):

    if(initial):
        for entry in entries:
            facility_repository.save(entry)
        return
    
    for entry in entries:
        if(entry['record_date'] == datetime.today().strftime('%Y-%m-%d')):
            facility_repository.save(entry)
            

# creates and return python objects from the fetched data
def fetch_to_db(initial = False):
    data = fetch()

    facility_objects = []

    for entry in data:
        facility = Facility(entry['center'], entry['center_search_status'], entry['facility'], entry['record_date'][:10], entry['country'], entry['contact'], entry['phone'], entry['location']['latitude'], entry['location']['longitude'], entry['location']['human_address'], entry['city'], entry['state'], entry['zipcode'], entry[':@computed_region_bigw_e76g'], entry[':@computed_region_cbhk_fwbd'], entry[':@computed_region_nnqa_25f4'])

        if('status' in entry.keys()):
            facility.status = entry['status']

        if('url_link' in entry.keys()):
            facility.url = entry['url_link']['url']

        if('occupied' in entry.keys()):
            facility.occupied = entry['occupied'][:10]

        if('last_update' in entry.keys()):
            facility.last_update = entry['last_update'][:10]

        facility_objects.append(facility)

    save_multiple_entries(facility_objects, initial)


# turns the data retrieved from the db to json format
def objects_to_json(objects):
    response = []

    for object in objects:
        response.append(object.__dict__)

    return jsonify(response)
