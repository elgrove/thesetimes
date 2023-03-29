import abc

from bs4 import BeautifulSoup


class Publication(abc.ABC):
    def __init__(self, parser=BeautifulSoup) -> None:
        self.parser = parser
        self.name = ""
        self.short_name = ""
        self.category = ""
        self.homepage = ""

    @abc.abstractmethod
    def get_articles(self, driver):
        ...

    @abc.abstractmethod
    def get_article_title(self, driver, url):
        ...

    @abc.abstractmethod
    def get_article_body(self, driver, url):
        ...

    @abc.abstractmethod
    def get_article_authors(self, driver, url):
        ...

    @abc.abstractmethod
    def get_article_pubdate(self, driver, url):
        ...
