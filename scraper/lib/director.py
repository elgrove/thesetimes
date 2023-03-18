from sqlalchemy.orm import sessionmaker
from scraper.lib.article import Article
from scraper.lib.article_scraper import ArticleScraper
from scraper.lib.database import get_db_engine
from scraper.lib.publications.financial_times import FinancialTimes
from scraper.lib.webdriver import WebDriverBuilder


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
        with self.session() as session:
            for pub in self.PUBLICATIONS:
                pub = pub()
                article_urls = pub.get_articles(self.driver)
                for url in article_urls:
                    scraper = self.article_scraper(pub, url, self.driver, session)
                    scraper.scrape_to_db()
