from lib.database import get_db_engine
from lib.logger import get_logger
from lib.webdriver import WebDriverBuilder
from lib.director import ScraperDirector


if __name__ == "__main__":
    scraper_director = ScraperDirector()
    scraper_director.run()
