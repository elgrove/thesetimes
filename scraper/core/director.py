from sqlalchemy.orm import sessionmaker

from core import LOGGER
from core.article_scraper import ArticleScraper
from core.database import get_db_engine
from core.publications.financial_times import FinancialTimes
from core.webdriver import WebDriverBuilder


class ScraperDirector:
    """Director class orchestrating scraping of all publications."""

    PUBLICATIONS = [FinancialTimes]

    def __init__(
        self,
        driver_builder=WebDriverBuilder,
        article_scraper=ArticleScraper,
        engine=get_db_engine(),
    ):
        """Initialise with webdriver and article scraper classes and db engine."""
        self.driver = driver_builder().get_driver()
        self.engine = engine
        self.article_scraper = article_scraper

    @property
    def session(self):
        """Returns SQLAlchemy session."""
        return sessionmaker(self.engine)

    def run(self):
        """Executes scraping of all publications."""
        LOGGER.info("Initiating database session")
        with self.session() as session:
            for pub in self.PUBLICATIONS:
                pub = pub()
                LOGGER.info("Working on publication %s", pub.name)
                article_urls = pub.get_articles(self.driver)
                for url in article_urls:
                    scraper = self.article_scraper(pub, url, self.driver, session)
                    scraper.scrape_to_db()
            LOGGER.info("Closing database session")
