from datetime import datetime

import pytest

from core.article_scraper import ArticleToScrape
from core.publication.economist import TheEconomist
from tests.cases.publications.economist.article import ARTICLE_HTML
from tests.cases.publications.economist.homepage import HOMEPAGE_HTML


class MockTheEconomistDriver:
    """Mocking the webdriver service, returning pages."""

    def __init__(self):
        """Initialise."""
        self.page_source = ""

    def get(self, url):
        """Mock webdriver.get method."""
        if url.endswith("economist.com"):
            self.page_source = HOMEPAGE_HTML
        else:
            self.page_source = ARTICLE_HTML


@pytest.mark.unit
class TestTheEconomist:
    """Tests for the The Economist scraper."""

    def test_get_articles_isobject_article(self):
        """Test get_articles."""
        pub = TheEconomist()
        driver = MockTheEconomistDriver()
        articles = pub.get_articles(driver)

        assert all(isinstance(article, ArticleToScrape) for article in articles)

    def test_get_articles_returns_count(self):
        pub = TheEconomist()
        driver = MockTheEconomistDriver()
        articles = pub.get_articles(driver)

        assert len(articles) == 7

    def test_get_articles_urls(self):
        pub = TheEconomist()
        driver = MockTheEconomistDriver()
        articles = pub.get_articles(driver)

        assert articles == [
            ArticleToScrape(
                url="https://www.economist.com/leaders/2023/11/23/how-to-thrive-in-a-fractured-world",
                page_rank=1,
            ),
            ArticleToScrape(
                url="https://www.economist.com/leaders/2023/11/22/the-fallout-from-the-weirdness-at-openai",
                page_rank=2,
            ),
            ArticleToScrape(
                url="https://www.economist.com/europe/2023/11/23/geert-wilderss-election-win-leaves-the-dutch-in-an-awful-quandary",
                page_rank=3,
            ),
            ArticleToScrape(
                url="https://www.economist.com/finance-and-economics/2023/11/22/another-crypto-boss-falls",
                page_rank=4,
            ),
            ArticleToScrape(
                url="https://www.economist.com/europe/2023/11/22/tyrant-liberator-warmonger-bureaucrat-the-meaning-of-napoleon",
                page_rank=5,
            ),
            ArticleToScrape(
                url="https://www.economist.com/united-states/2023/11/22/spending-on-infrastructure-has-fallen-in-real-terms-in-america",
                page_rank=6,
            ),
            ArticleToScrape(
                url="https://www.economist.com/obituary/2023/11/22/elinor-otto-did-not-realise-what-giant-strides-she-was-making-for-women",
                page_rank=7,
            ),
        ]

    def test_get_articles_exclude_news_in_brief(self):
        pub = TheEconomist()
        driver = MockTheEconomistDriver()
        articles = pub.get_articles(driver)

        assert "https://www.economist.com/the-world-in-brief" not in [
            a.url for a in articles
        ]

    def test_get_article_title(self):
        pub = TheEconomist()
        driver = MockTheEconomistDriver()
        title = pub.get_article_title(driver, "url")
        assert (
            title
            == "How to thrive in a fractured world"
        )

    def test_get_article_authors(self):
        pub = TheEconomist()
        driver = MockTheEconomistDriver()
        authors = pub.get_article_authors(driver, "url")
        assert authors == "The Economist Staff"

    def test_get_article_pubdate(self):
        pub = TheEconomist()
        driver = MockTheEconomistDriver()
        pubdate = pub.get_article_pubdate(
            driver,
            "https://www.economist.com/leaders/2023/11/23/how-to-thrive-in-a-fractured-world",
        )
        assert pubdate == datetime(2023, 11, 23, 5, 0, 0)

    def test_get_article_body(self):
        pub = TheEconomist()
        driver = MockTheEconomistDriver()
        body = pub.get_article_body(driver, "url")
        assert len(body) == 12
