from db.run_sql import sql_runner
from models.facility import Facility

# This file handles the construction of sql queries using prepared statements

# save a Facility object to the DB
def save(facility):
    sql = "INSERT INTO facilities (center, center_search_status, facility, occupied, status, url, record_date, last_update, country, contact, phone, latitude, longitude, human_address, city, state, zipcode, computed_region_bigw_e76g, computed_region_cbhk_fwbd, computed_region_nnqa_25f4) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?) RETURNING *"

    values = [
        facility.center, facility.center_search_status, facility.facility, facility.occupied, facility.status, facility.url, facility.record_date, facility.last_update, facility.country, facility.contact, facility.phone, facility.latitude, facility.longitude, facility.human_address, facility.city, facility.state, facility.zipcode, facility.computed_region_bigw_e76g, facility.computed_region_cbhk_fwbd, facility.computed_region_nnqa_25f4
        ]

    result = sql_runner(sql, values)
    id = result[0]['id']
    facility.id = id
    return facility

# return all entried from the facilities table and instantiate Facility objects from the row data
def select_all():
    facilities = []

    sql = "SELECT * FROM facilities WHERE status = ?"
    values = ["Active"]
    results = sql_runner(sql, values)

    for row in results:
        facility = Facility(row['center'], row['center_search_status'], row['facility'], row['record_date'], row['country'], row['contact'], row['phone'], row['latitude'], row['longitude'], row['human_address'], row['city'], row['state'], row['zipcode'], row['computed_region_bigw_e76g'], row['computed_region_cbhk_fwbd'], row['computed_region_nnqa_25f4'], row['occupied'], row['last_update'], row['status'], row['url'], row['id'])

        facilities.append(facility)

    
    return facilities


# Return a single entry from the DB by ID, instantiating a Facility object from the data
def select(id):
    facility = None

    sql = "SELECT * FROM facilities WHERE id = ?"
    values = [id]
    result = sql_runner(sql, values)[0]

    if(result != None):
        facility = Facility(result['center'], result['center_search_status'], result['facility'], result['record_date'], result['country'], result['contact'], result['phone'], result['latitude'], result['longitude'], result['human_address'], result['city'], result['state'], result['zipcode'], result['computed_region_bigw_e76g'], result['computed_region_cbhk_fwbd'], result['computed_region_nnqa_25f4'], result['occupied'], result['last_update'], result['status'], result['url'], result['id'])
    
    return facility

# Updates the data of a specific DB entry, found by ID
def update(facility):
    sql = "UPDATE facilities SET (center, center_search_status, facility, occupied, status, url, record_date, last_update, country, contact, phone, latitude, longitude, human_address, city, state, zipcode, computed_region_bigw_e76g, computed_region_cbhk_fwbd, computed_region_nnqa_25f4) = (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?) WHERE id = ?"

    values = [facility.center, facility.center_search_status, facility.facility, facility.occupied, facility.status, facility.url, facility.record_date, facility.last_update, facility.country, facility.contact, facility.phone, facility.latitude, facility.longitude, facility.human_address, facility.city, facility.state, facility.zipcode, facility.computed_region_bigw_e76g, facility.computed_region_cbhk_fwbd, facility.computed_region_nnqa_25f4, facility.id]

    sql_runner(sql, values)