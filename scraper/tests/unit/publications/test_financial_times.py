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

        assert len(article_urls) == 13
        assert all(a in article_urls for a in [
            # top story
            "https://www.ft.com/content/59827e3a-ca68-4c75-a6c6-b71d58df907a",
            # second shelf
            "https://www.ft.com/content/69ca2924-85f7-42ae-9b5b-5b9907cf12b7",
            # spotlight shelf
            "https://www.ft.com/content/b1657ee3-eb9d-41c7-851e-5900c74bd934",
            # # news shelf
            # "https://www.ft.com/content/f814ff18-4c05-4589-9879-b0800ac3a4ed",
            # "https://www.ft.com/content/475e8cc1-8cd5-4877-980e-7a86847e3bc6"
            ])

    def test_get_articles_exclude_live_news(self):
        pub = FinancialTimes()
        driver = MockFinancialTimesDriver()
        article_urls = pub.get_articles(driver)
        assert (
            "https://www.ft.com/content/9232fa8b-ef69-4ccb-abe0-58f69eb726b1"
            not in article_urls
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
