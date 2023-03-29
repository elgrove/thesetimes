from core.database import get_db_engine
from core.logger import get_logger
from core.webdriver import WebDriverBuilder
from core.director import ScraperDirector


if __name__ == "__main__":
    scraper_director = ScraperDirector()
    scraper_director.run()
