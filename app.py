from flask import Flask
import schedule
from datetime import datetime
from helpers.helper_functions import fetch, fetch_to_db, objects_to_json
import repositories.facility_repository as facility_repository


app = Flask(__name__)

# schedules a new fetch to be called each day
schedule.every().day.at('23:50').do(fetch_to_db)

# fetching and saving to db on launch. No pun intended.
fetch_to_db(True)

@app.route('/api/', methods=['GET'])
def main_endpoint():

    # retrieve data from db and return as json
    db_data = facility_repository.select_all()
    formatted_data = objects_to_json(db_data)
    return formatted_data


if __name__ == '__main__':
    app.config['JSON_SORT_KEYS'] = False
    app.run(debug=True)
    with app.app_context():
        main_endpoint()
        
