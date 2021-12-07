from requests import api
import schedule
import time
from utils.update import update_db
from utils.update import api_url
import requests


schedule.every().day.at("01:50").do(update_db)
schedule.every().day.at("06:50").do(update_db)
schedule.every().day.at("09:50").do(update_db)
schedule.every().day.at("12:50").do(update_db)
schedule.every().day.at("14:50").do(update_db)
schedule.every().day.at("16:50").do(update_db)
schedule.every().day.at("18:50").do(update_db)


# schedule.every(4).hours.do(update_db)

if __name__ == "__main__":
    time.sleep(8)  # wait for api to come online

    # # testing
    # update_db()

    r = requests.get(api_url)
    # check if db is empty, if so do first run
    if len(r.json()) == 0:
        update_db()

    while True:
        schedule.run_pending()
        time.sleep(1)
