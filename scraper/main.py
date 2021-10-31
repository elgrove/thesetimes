import schedule
import time
from utils.update import update_db


schedule.every().day.at("07:00").do(update_db)
schedule.every().day.at("12:00").do(update_db)
schedule.every().day.at("16:00").do(update_db)
schedule.every().day.at("19:00").do(update_db)


if __name__ == "__main__":
    # update_db()
    while True:
        schedule.run_pending()
        time.sleep(1)
