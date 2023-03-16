import abc


class Publication(abc.ABC):
    def __init__(self) -> None:
        self.name = "Financial Times"
        self.short_name = "ft"
        self.category = "News"
        self.homepage = "https://www.ft.com"

    @abc.abstractmethod
    def get_articles(self, driver):
        ...

    @abc.abstractmethod
    def get_article_title(self, driver, url):
        ...

    @abc.abstractmethod
    def get_article_body(self, driver):
        ...

    @abc.abstractmethod
    def get_article_authors(self, driver):
        ...

    @abc.abstractmethod
    def get_article_pubdate(self, driver):
        ...
