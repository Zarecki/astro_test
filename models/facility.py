# consider - using descrtucturing syntax in parameters. Use standard form if no improved legibility

class Facility:
    def __init__(self, center, center_search_status, facility, record_date, country, contact, phone, latitude, longitude, human_address, city, state, zipcode, computed_region_bigw_e76g, computed_region_cbhk_fwbd, computed_region_nnqa_25f4, occupied = None, last_update = None, status = None, url = None, id = None):
        self.id = id
        self.center = center
        self.center_search_status = center_search_status
        self.facility = facility
        self.occupied = occupied
        self.status = status
        self.url = url
        self.record_date = record_date
        self.last_update = last_update
        self.country = country
        self.contact = contact
        self.phone = phone
        self.latitude = latitude
        self.longitude = longitude
        self.human_address = human_address
        self.city = city
        self.state = state
        self.zipcode = zipcode
        self.computed_region_bigw_e76g = computed_region_bigw_e76g
        self.computed_region_cbhk_fwbd = computed_region_cbhk_fwbd
        self.computed_region_nnqa_25f4 =computed_region_nnqa_25f4