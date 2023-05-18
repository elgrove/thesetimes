# pylint: skip-file

import abc
from datetime import datetime

from bs4 import BeautifulSoup


class Publication(abc.ABC):
    """Abstract class laying blueprint for classes holding code specific to each Publication.

    All methods take a WebDriver object to be controlled, and those that act on a single article also
        take the article URL.
    """

    def __init__(self, parser=BeautifulSoup) -> None:
        """Initialise the abstract class with necessary attributes."""

        self.parser = parser
        self.name = ""
        self.short_name = ""
        self.category = ""
        self.homepage = ""

    @abc.abstractmethod
    def get_articles(self, driver) -> list:
        """Abstract method for getting a list of article URLs to be scraped from this publication."""
        ...

    @abc.abstractmethod
    def get_article_title(self, driver, article_url) -> str:
        """Abstract method for getting an article's title, as a string."""
        ...

    @abc.abstractmethod
    def get_article_body(self, driver, article_url) -> list:
        """Abstract method for getting an article body as a list of strings, one for each paragraph."""
        ...

    @abc.abstractmethod
    def get_article_authors(self, driver, article_url) -> str:
        """Abstract method for getting an article's authors, as a comma delimited string."""
        ...

    @abc.abstractmethod
    def get_article_pubdate(self, driver, article_url) -> datetime:
        """Abstract method for getting an article's published date, as a datetime object."""
        ...
