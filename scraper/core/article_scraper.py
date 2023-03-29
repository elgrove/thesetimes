import logging

from core.logger import get_logger
from functools import cached_property
from core.database_models import Article
from core.publications import Publication

from . import LOGGER


class ArticleScraper:
    def __init__(self, publication: Publication, url, driver, session):
        self.publication = publication
        self.url = url
        self.driver = driver
        self.session = session

    @cached_property
    def authors(self):
        return self.publication.get_article_authors(self.driver, self.url)

    @cached_property
    def title(self):
        return self.publication.get_article_title(self.driver, self.url)

    @cached_property
    def body(self):
        return self.publication.get_article_body(self.driver, self.url)

    @cached_property
    def published_date(self):
        return self.publication.get_article_pubdate(self.driver, self.url)

    @property
    def database_model(self):
        return Article(
            publication_name=self.publication.name,
            publication_short=self.publication.short_name,
            title=self.title,
            body=self.body,
            authors=self.authors,
            published_date=self.published_date,
        )

    def scrape_to_db(self):
        LOGGER.info(f"Adding to session article {self.title}")
        self.session.add(self.database_model)
        LOGGER.info(f"Committing session")
        self.session.commit()
