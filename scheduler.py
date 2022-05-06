import schedule
import time
from helpers.helper_functions import fetch_to_db


schedule.every(1).minutes.do(fetch_to_db)

while True:
 
    # Checks whether a scheduled task
    # is pending to run or not
    schedule.run_pending()
    time.sleep(1)

# fetching and saving to db on launch. No pun intended.
fetch_to_db(True)