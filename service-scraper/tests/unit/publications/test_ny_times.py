from datetime import datetime

import pytest

from core.article_scraper import ArticleToScrape
from core.publication.ny_times import NewYorkTimes
from tests.cases.publications.ny_times.article import ARTICLE_HTML
from tests.cases.publications.ny_times.homepage import HOMEPAGE_HTML


class MockNewYorkTimesDriver:
    """Mocking the webdriver service, returning pages from the NYT."""

    def __init__(self):
        """Initialise."""
        self.page_source = ""

    def get(self, url):
        """Mock webdriver.get method."""
        if url.endswith("nytimes.com"):
            self.page_source = HOMEPAGE_HTML
        else:
            self.page_source = ARTICLE_HTML


@pytest.mark.unit
class TestNewYorkTimes:
    """Tests for the NYT scraper."""

    def test_get_articles_isobject_article(self):
        """Test get_articles."""
        pub = NewYorkTimes()
        driver = MockNewYorkTimesDriver()
        articles = pub.get_articles(driver)

        assert all(isinstance(article, ArticleToScrape) for article in articles)

    def test_get_articles_count(self):
        pub = NewYorkTimes()
        driver = MockNewYorkTimesDriver()
        articles = pub.get_articles(driver)

        assert len(articles) == 10

    def test_get_articles_urls(self):
        pub = NewYorkTimes()
        driver = MockNewYorkTimesDriver()
        article_urls = [a.url for a in pub.get_articles(driver)]

        assert article_urls == [
            "https://www.nytimes.com/2023/05/29/business/debt-ceiling-agreement.html",
            "https://www.nytimes.com/2023/05/29/us/politics/debt-ceiling-economy.html",
            "https://www.nytimes.com/2023/05/29/us/politics/north-dakota-teen-death-right-wing-trump.html",
            "https://www.nytimes.com/2023/05/29/world/asia/japan-sexual-harassment-women.html",
            "https://www.nytimes.com/2023/05/29/arts/television/succession-matthew-macfadyen-nicholas-braun-tom-and-greg.html",
            "https://www.nytimes.com/2023/05/28/arts/television/succession-series-finale-recap.html",
            "https://www.nytimes.com/2023/05/29/us/tina-turner-hometown-tennessee-nutbush.html",
            "https://www.nytimes.com/2023/05/29/world/asia/van-gogh-china-buyer.html",
            "https://www.nytimes.com/2023/05/29/us/politics/supreme-court-high-school-admissions.html",
            "https://www.nytimes.com/2023/05/28/us/housing-crisis-provincetown-rent.html",
        ]

    def test_get_article_authors(self):
        """Test get article authors."""
        pub = NewYorkTimes()
        driver = MockNewYorkTimesDriver()
        authors = pub.get_article_authors(driver, "url")
        assert authors == "Jim Tankersley, Alan Rappeport"

    def test_get_article_pubdate(self):
        pub = NewYorkTimes()
        driver = MockNewYorkTimesDriver()
        pubdate = pub.get_article_pubdate(driver, "url")
        assert pubdate == datetime(2023, 5, 29, 17, 7, 32)

    def test_get_article_title(self):
        pub = NewYorkTimes()
        driver = MockNewYorkTimesDriver()
        title = pub.get_article_title(driver, "url")
        assert (
            title
            == "New Details in Debt Limit Deal: Where $136 Billion in Cuts Will Come From"
        )

    def test_get_article_body(self):
        pub = NewYorkTimes()
        driver = MockNewYorkTimesDriver()
        body = pub.get_article_body(driver, "url")
        assert len(body) == 45
        assert (
            body[0]
            == "The full legislative text of Speaker Kevin McCarthy’s agreement in principle with President Biden to suspend the nation’s borrowing limit revealed new and important details about the deal, which House lawmakers are expected to vote on this week."
        )
        assert (
            body[-1]
            == "Republicans wanted much deeper spending cuts and stricter work requirements. They also wanted to repeal of hundreds of billions of dollars in tax incentives signed by Mr. Biden to accelerate the transition to lower-emission energy sources and fight climate change. Mr. Biden wanted to raise taxes on corporations and high earners, and to take new steps to reduce Medicare’s spending on prescription drugs. None of those made it into the deal."
        )
