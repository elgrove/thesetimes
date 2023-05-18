from dataclasses import dataclass
from datetime import datetime

from core import LOGGER
from core.database_models import Article as ArticleModel
from core.publication import Publication


@dataclass
class ArticleToScrape:
    url: str
    page_rank: int


class ArticleScraper:
    """Class for scraping an article from any publication."""

    def __init__(self, publication: Publication, url: ArticleToScrape, driver, session):
        """Initialise with publication class, url of article, scraper webdriver and db session."""
        self.publication = publication
        self.url = url
        self.driver = driver
        self.session = session

    @property
    def authors(self):
        """Returns the article's authors."""
        return self.publication.get_article_authors(self.driver, self.url)

    @property
    def title(self):
        """Returns the article's title."""
        return self.publication.get_article_title(self.driver, self.url)

    @property
    def body(self):
        """Returns the article's body as a list of paragraphs."""
        return self.publication.get_article_body(self.driver, self.url)

    @property
    def published_date(self):
        """Returns the article's publication datetime."""
        return self.publication.get_article_pubdate(self.driver, self.url)

    @property
    def database_model(self):
        """Returns a database model of the article."""
        return ArticleModel(
            publication_name=self.publication.name,
            publication_short=self.publication.short_name,
            url=self.url,
            title=self.title,
            body=self.body,
            authors=self.authors,
            published_date=self.published_date,
        )

    def scrape_to_db(self):
        """Execute scraping and insert article object into database."""
        LOGGER.debug("Merging into session: %s", self.title)
        result = self.session.merge(self.database_model)
        if result in self.session.dirty:
            LOGGER.info("Article was updated: %s", self.title)
        elif result in self.session.new:
            LOGGER.info("Article was inserted: %s ", self.title)

        LOGGER.debug("Committing session")
        self.session.commit()
