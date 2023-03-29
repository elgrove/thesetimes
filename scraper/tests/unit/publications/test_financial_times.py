from datetime import datetime

import pytest

from core.publications.financial_times import FinancialTimes
from tests.cases.publications.cases_financial_times import HOMEPAGE_HTML, ARTICLE_HTML


class MockFinancialTimesDriver:
    def __init__(self):
        self.page_source = ""

    def get(self, url):
        if url.endswith("ft.com"):
            self.page_source = HOMEPAGE_HTML
        else:
            self.page_source = ARTICLE_HTML


@pytest.mark.unit
class TestFinancialTimes:
    def test_get_articles(self):
        pub = FinancialTimes()
        driver = MockFinancialTimesDriver()
        article_urls = pub.get_articles(driver)
        assert (
            article_urls[0]
            == "https://www.ft.com/content/5746165a-3a0c-42c7-9a2e-cb7cf5f33f46"
        )

    def test_get_article_authors(self):
        pub = FinancialTimes()
        driver = MockFinancialTimesDriver()
        authors = pub.get_article_authors(driver, "url")
        assert authors == "Kate Duguid"

    def test_get_article_pubdate(self):
        pub = FinancialTimes()
        driver = MockFinancialTimesDriver()
        pubdate = pub.get_article_pubdate(driver, "url")
        assert pubdate == datetime(2023, 3, 17, 21, 0, 24)

    def test_get_article_title(self):
        pub = FinancialTimes()
        driver = MockFinancialTimesDriver()
        title = pub.get_article_title(driver, "url")
        assert (
            title == "US Treasuries’ rollercoaster ride strains bond market functioning"
        )

    def test_get_article_body(self):
        pub = FinancialTimes()
        driver = MockFinancialTimesDriver()
        body = pub.get_article_body(driver, "url")
        assert len(body) == 20
