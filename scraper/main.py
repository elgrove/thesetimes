import schedule
import time
from utils.update import update_db

schedule.every(2).hours.do(update_db)

if __name__ == "__main__":
    update_db()
    while True:
        schedule.run_pending()
        time.sleep(1)
