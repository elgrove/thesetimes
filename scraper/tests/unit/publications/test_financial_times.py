from datetime import datetime

import pytest

from core.publication.financial_times import FinancialTimes
from tests.cases.publications.cases_financial_times import HOMEPAGE_HTML, ARTICLE_HTML


import pytest
from sqlalchemy import create_mock_engine


@pytest.fixture(name="article", autouse=True)
def article(monkeypatch):
    class Article:
        def __init__(self, *args, **kwargs):
            pass

    monkeypatch.setattr("core.database_models.Article", Article)


@pytest.fixture(name="engine", autouse=True)
def engine(monkeypatch):
    def get_engine():
        return create_mock_engine("postgresql://", lambda x: x)

    monkeypatch.setattr("core.database.engine.get_db_engine", get_engine)


class MockFinancialTimesDriver:
    """Mocking the webdriver service, returning pages from the FT."""

    def __init__(self):
        """Initialise."""
        self.page_source = ""

    def get(self, url):
        """Mock webdriver.get method."""
        if url.endswith("ft.com"):
            self.page_source = HOMEPAGE_HTML
        else:
            self.page_source = ARTICLE_HTML


@pytest.mark.unit
class TestFinancialTimes:
    """Tests for the Financial Times scraper."""

    def test_get_articles(self):
        """Test get_articles."""
        pub = FinancialTimes()
        driver = MockFinancialTimesDriver()
        article_urls = pub.get_articles(driver)

        assert len(article_urls) == 13
        assert all(
            a in article_urls
            for a in [
                # top story
                "https://www.ft.com/content/59827e3a-ca68-4c75-a6c6-b71d58df907a",
                # second shelf
                "https://www.ft.com/content/69ca2924-85f7-42ae-9b5b-5b9907cf12b7",
                # spotlight shelf
                "https://www.ft.com/content/b1657ee3-eb9d-41c7-851e-5900c74bd934",
                # # news shelf
                # "https://www.ft.com/content/f814ff18-4c05-4589-9879-b0800ac3a4ed",
                # "https://www.ft.com/content/475e8cc1-8cd5-4877-980e-7a86847e3bc6"
            ]
        )

    def test_get_articles_exclude_live_news(self):
        """Test get articles, excluding live news feed pages."""
        pub = FinancialTimes()
        driver = MockFinancialTimesDriver()
        article_urls = pub.get_articles(driver)
        assert (
            "https://www.ft.com/content/9232fa8b-ef69-4ccb-abe0-58f69eb726b1"
            not in article_urls
        )

    def test_get_articles_order(self):
        pass

    def test_get_article_authors(self):
        """Test get article authors."""
        pub = FinancialTimes()
        driver = MockFinancialTimesDriver()
        authors = pub.get_article_authors(driver, "url")
        assert authors == "Kate Duguid"

    def test_get_article_pubdate(self):
        """Test get article published date."""
        pub = FinancialTimes()
        driver = MockFinancialTimesDriver()
        pubdate = pub.get_article_pubdate(driver, "url")
        assert pubdate == datetime(2023, 3, 17, 21, 0, 24)

    def test_get_article_title(self):
        """Test get article title."""
        pub = FinancialTimes()
        driver = MockFinancialTimesDriver()
        title = pub.get_article_title(driver, "url")
        assert (
            title == "US Treasuries’ rollercoaster ride strains bond market functioning"
        )

    def test_get_article_body(self):
        """Test get article body."""
        pub = FinancialTimes()
        driver = MockFinancialTimesDriver()
        body = pub.get_article_body(driver, "url")
        assert len(body) == 20
