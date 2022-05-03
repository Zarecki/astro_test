from db.run_sql import run_sql

from models.facility import Facility

def save(facility):
    sql = "INSERT INTO facilities (center, center_search_status, facility, occupied, status, url, record_date, last_update, country, contact, phone, latitude, longitude, human_address, city, state, zipcode, computed_region_bigw_e76g, computed_region_cbhk_fwbd, computed_region_nnqa_25f4) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?) RETURNING *"
    values = [facility.center, facility.center_search_status, facility.facility, facility.occupied, facility.status, facility.url, facility.record_date, facility.last_update, facility.country, facility.contact, facility.phone, facility.latitude, facility.longitude, facility.human_address, facility.city, facility.state, facility.zipcode, facility.computed_region_bigw_e76g, facility.computed_region_cbhk_fwbd, facility.computed_region_nnqa_25f4]
    result = run_sql(sql, values)
    id = result[0]['id']
    facility.id = id
    return facility