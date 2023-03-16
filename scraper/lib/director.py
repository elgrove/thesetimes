from functools import cached_property

import sqlalchemy
from sqlalchemy.orm import sessionmaker

from scraper.lib.article import Article
from scraper.lib.article_scraper import ArticleScraper
from scraper.lib.publications.financial_times import FinancialTimes
from sqlalchemy.orm import Session

from scraper.lib.webdriver import WebDriverBuilder


class ScraperDirector:
    PUBLICATIONS = [FinancialTimes]

    def __init__(self, driver_builder=WebDriverBuilder, article_scraper=ArticleScraper):
        self.driver = driver_builder().get_driver()
        self.article_scraper = article_scraper

    @cached_property
    def engine(self):
        """"""
        # url = URL()
        # return sqlalchemy.create_engine()

    @property
    def session(self):
        return sessionmaker(self.engine)

    def run(self):
        with self.session() as session:
            for pub in self.PUBLICATIONS:
                pub = pub()
                article_urls = pub.get_articles(self.driver)
                for url in article_urls:
                    scraper = self.article_scraper(pub, url, self.driver, self.session)
                    scraper.scrape_to_db()
