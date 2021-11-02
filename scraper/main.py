from requests import api
import schedule
import time
from utils.update import update_db
from utils.update import api_url
import requests

# schedule.every().day.at("07:00").do(update_db)
# schedule.every().day.at("12:00").do(update_db)
# schedule.every().day.at("17:00").do(update_db)

schedule.every().hour.at(":55").do(update_db)

if __name__ == "__main__":
    time.sleep(4)  # wait for api to come online

    # testing
    update_db()

    r = requests.get(api_url)
    # check if db is empty, if so do first run
    if len(r.json()) == 0:
        update_db()

    while True:
        schedule.run_pending()
        time.sleep(1)
