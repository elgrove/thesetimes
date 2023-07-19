# pylint: skip-file

import abc
from datetime import datetime

from bs4 import BeautifulSoup


class Publication(abc.ABC):
    """Abstract class laying blueprint for classes holding code specific to each
    Publication.

    All methods take a WebDriver object to be controlled, and those that act on a single
    article     also take the article URL.

    Some methods offer a default implementation based on common meta tags that     most
    publications use in their header.

    OTOH, get_articles and get_article_body will almost certainly require custom
    implementation.
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
        """Abstract method for getting a list of article URLs to be scraped from this
        publication."""
        ...

    @abc.abstractmethod
    def get_article_body(self, driver, article_url) -> list:
        """Abstract method for getting an article body as a list of strings, one for
        each paragraph."""
        ...

    def get_article_title(self, driver, article_url) -> str:
        """Abstract method for getting an article's title, as a string.

        Default implementation uses a meta tag in the html header that most publications
        have.
        """
        driver.get(article_url)
        soup = self.parser(driver.page_source.encode("utf-8"), "lxml")
        title = str.rstrip(soup.find("meta", property="og:title")["content"])
        return title

    def get_article_authors(self, driver, article_url) -> str:
        """Abstract method for getting an article's authors, as a comma delimited
        string.

        Default implementation uses a meta tag in the html header that most publications
        have.
        """
        driver.get(article_url)
        soup = self.parser(driver.page_source.encode("utf-8"), "lxml")
        author_count = len(soup.find_all("meta", property="article:author"))

        if not author_count:
            return f"{self.name} Staff"

        if author_count == 0:
            return f"{self.name} Staff"
        elif author_count > 1:
            authors = []
            for n in soup.find_all("meta", property="article:author"):
                authors.append(n["content"])
                author = ", ".join(authors)
        else:
            author = soup.find("meta", property="article:author")["content"]
        return author

    def get_article_pubdate(self, driver, article_url) -> datetime:
        """Abstract method for getting an article's published date, as a datetime
        object.

        Default implementation uses a meta tag in the html header that most publications
        have.
        """
        driver.get(article_url)
        soup = self.parser(driver.page_source.encode("utf-8"), "lxml")
        pubdate = datetime.strptime(
            soup.find("meta", property="article:modified_time")["content"],
            "%Y-%m-%dT%H:%M:%S.%fZ",
        )
        if pubdate.microsecond:
            pubdate = pubdate.replace(microsecond=0)
        return pubdate
