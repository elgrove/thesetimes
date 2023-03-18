import logging
from sqlalchemy.orm import sessionmaker
from lib.article import Article
from lib.article_scraper import ArticleScraper
from lib.database import get_db_engine
from lib.publications.financial_times import FinancialTimes
from lib.webdriver import WebDriverBuilder
from . import LOGGER


class ScraperDirector:
    PUBLICATIONS = [FinancialTimes]

    def __init__(
        self,
        driver_builder=WebDriverBuilder,
        article_scraper=ArticleScraper,
        engine=get_db_engine(),
    ):
        self.driver = driver_builder().get_driver()
        self.engine = engine
        self.article_scraper = article_scraper

    @property
    def session(self):
        return sessionmaker(self.engine)

    def run(self):
        LOGGER.info("Initiating database session")
        with self.session() as session:
            for pub in self.PUBLICATIONS:
                pub = pub()
                LOGGER.info(f"Working on publication {pub.name}")
                article_urls = pub.get_articles(self.driver)
                for url in article_urls:
                    scraper = self.article_scraper(pub, url, self.driver, session)
                    scraper.scrape_to_db()
            LOGGER.info("Closing database session")
