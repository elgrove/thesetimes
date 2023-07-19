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
                url="https://www.economist.com/science-and-technology/2023/07/19/are-the-current-heatwaves-evidence-that-climate-change-is-speeding-up",
                page_rank=1,
            ),
            ArticleToScrape(
                url="https://www.economist.com/leaders/2023/07/19/the-world-economy-is-still-in-danger",
                page_rank=2,
            ),
            ArticleToScrape(
                url="https://www.economist.com/international/2023/07/19/what-if-china-and-india-became-friends",
                page_rank=3,
            ),
            ArticleToScrape(
                url="https://www.economist.com/asia/2023/07/19/an-american-soldier-has-deserted-to-north-korea",
                page_rank=4,
            ),
            ArticleToScrape(
                url="https://www.economist.com/business/2023/07/19/hollywoods-blockbuster-strike-may-become-a-flop",
                page_rank=5,
            ),
            ArticleToScrape(
                url="https://www.economist.com/graphic-detail/2023/07/19/brexit-was-wrong-say-57-of-british-voters",
                page_rank=6,
            ),
            ArticleToScrape(
                url="https://www.economist.com/technology-quarterly/2023/07/17/the-fertility-sector-is-booming",
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
            == "Are the current heatwaves evidence that climate change is speeding up?"
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
            "https://www.economist.com/science-and-technology/2023/07/19/are-the-current-heatwaves-evidence-that-climate-change-is-speeding-up",
        )
        assert pubdate == datetime(2023, 7, 19, 5, 0, 0)

    def test_get_article_body(self):
        pub = TheEconomist()
        driver = MockTheEconomistDriver()
        body = pub.get_article_body(driver, "url")
        assert len(body) == 23
