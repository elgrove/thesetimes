from dataclasses import dataclass
from datetime import datetime

from core import LOGGER
from core.database_models import Article
from core.publication import Publication


@dataclass
class ArticleToScrape:
    url: str
    page_rank: int


class ArticleScraper:
    """Class for scraping an article from any publication."""

    def __init__(
        self, publication: Publication, article: ArticleToScrape, driver, session
    ):
        """Initialise with publication class, url of article, scraper webdriver and db session."""
        self.publication = publication
        self.article = article
        self.driver = driver
        self.session = session

    @property
    def article_authors(self):
        """Returns the article's authors."""
        return self.publication.get_article_authors(self.driver, self.article.url)

    @property
    def article_title(self):
        """Returns the article's title."""
        return self.publication.get_article_title(self.driver, self.article.url)

    @property
    def article_body(self):
        """Returns the article's body as a list of paragraphs."""
        return self.publication.get_article_body(self.driver, self.article.url)

    @property
    def article_published_date(self):
        """Returns the article's publication datetime."""
        return self.publication.get_article_pubdate(self.driver, self.article.url)

    @property
    def article_database_model(self):
        """Returns a database model of the article."""
        return Article(
            publication_name=self.publication.name,
            publication_short=self.publication.short_name,
            url=self.article.url,
            title=self.article_title,
            body=self.article_body,
            authors=self.article_authors,
            published_date=self.article_published_date,
            page_rank=self.article.page_rank,
        )

    def scrape_to_db(self):
        """Execute scraping and insert article object into database."""
        LOGGER.debug("Merging into session: %s", self.article_title)
        result = self.session.merge(self.article_database_model)
        if result in self.session.dirty:
            LOGGER.info("Article was updated: %s", self.article_title)
        elif result in self.session.new:
            LOGGER.info("Article was inserted: %s ", self.article_title)

        LOGGER.debug("Committing session")
        self.session.commit()
