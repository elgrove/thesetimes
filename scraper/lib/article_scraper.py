from lib.article import Article
from lib.publications import Publication


class ArticleScraper:
    def __init__(self, publication: Publication, url, driver, session):
        self.publication = publication
        self.url = url
        self.driver = driver
        self.session = session

    @property
    def authors(self):
        return self.publication.get_article_authors(self.driver, self.url)

    @property
    def title(self):
        return self.publication.get_article_title(self.driver, self.url)

    @property
    def body(self):
        return self.publication.get_article_body(self.driver, self.url)

    @property
    def pubdate(self):
        return self.publication.get_article_pubdate(self.driver, self.url)


    @property
    def database_model(self):
        return Article(
            publication=self.publication.name,
            title=self.title,
            body=self.body,
            authors=self.authors,
            pubdate=self.pubdate,
        )

    def scrape_to_db(self):
        self.session.add(self.database_model)
        self.session.commit()
