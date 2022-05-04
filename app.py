from flask import Flask 

from helpers.fetch import fetch
import repositories.facility_repository as facility_repository
from models.facility import Facility


app = Flask(__name__)

data = fetch()
print(data[0])

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

    facility_repository.save(facility)

test = facility_repository.select_all()
print(test)
print(test[0])


if __name__ == '__main__':
    app.run(debug=True)