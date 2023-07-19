import os
from time import sleep

import schedule

from core.director import ScraperDirector


def main():
    """Entry point for the scraper container.

    Runs on startup then every n hours as defined by an env var.
    """
    scraper = ScraperDirector()
    scraper.run()
    scrape_interval = int(os.environ["SCRAPE_INTERVAL_HR"])
    schedule.every(scrape_interval).hours.do(scraper.run)
    while True:
        schedule.run_pending()
        sleep(1)


if __name__ == "__main__":
    main()
