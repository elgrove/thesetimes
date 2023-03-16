from scraper.lib.article import Article
from scraper.lib.publications import Publication


class ArticleScraper:
    def __init__(self, publication: Publication, url, driver, session):
        self.publication = publication
        self.url = url

    @property
    def title(self):
        return self.publication.get_article_title(self.url)

    @property
    def body(self):
        return self.publication.get_article_body(self.url)

    @property
    def pubdate(self):
        return self.publication.get_article_pubdate(self.url)

    @property
    def authors(self):
        return self.publication.get_article_authors(self.url)

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
        session.add(self.database_model)
        session.commit()
