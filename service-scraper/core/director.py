from sqlalchemy.orm import sessionmaker

from core import LOGGER
from core.article_scraper import ArticleScraper
from core.database import get_db_engine
from core.publication.financial_times import FinancialTimes
from core.publication.new_yorker import TheNewYorker
from core.webdriver import WebDriverBuilder


class ScraperDirector:
    """Director class orchestrating scraping of all publications."""

    PUBLICATIONS = [FinancialTimes, TheNewYorker]

    def __init__(
        self,
        driver_builder=WebDriverBuilder,
        article_scraper=ArticleScraper,
        engine=get_db_engine,
    ):
        """Initialise with webdriver and article scraper classes and db engine."""
        self.driver = driver_builder().get_driver()
        self.engine = engine()
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
                try:
                    articles = pub.get_articles(self.driver)
                except:
                    LOGGER.error("Get articles failed for publication %s", pub.name)
                for article in articles:
                    try:
                        self.article_scraper(
                            pub, article, self.driver, session
                        ).scrape_to_db()
                    except:
                        LOGGER.error("Scrape failed for %s", article.url)
            LOGGER.info("Closing database session")
        self.driver.quit()
