from datetime import datetime

import pytest

from core.article_scraper import ArticleToScrape
from core.publication.new_yorker import TheNewYorker
from tests.cases.publications.new_yorker.article import ARTICLE_HTML
from tests.cases.publications.new_yorker.homepage import HOMEPAGE_HTML


class MockNewYorkerDriver:
    """Mocking the webdriver service, returning pages from the FT."""

    def __init__(self):
        """Initialise."""
        self.page_source = ""

    def get(self, url):
        """Mock webdriver.get method."""
        if url.endswith("newyorker.com"):
            self.page_source = HOMEPAGE_HTML
        else:
            self.page_source = ARTICLE_HTML


@pytest.mark.unit
class TestNewYorker:
    """Tests for the New Yorker scraper."""

    def test_get_articles_isobject_article(self):
        """Test get_articles."""
        pub = TheNewYorker()
        driver = MockNewYorkerDriver()
        articles = pub.get_articles(driver)

        assert all(isinstance(article, ArticleToScrape) for article in articles)

    def test_get_articles_count(self):
        """Test get articles returns 9 articles."""
        pub = TheNewYorker()
        driver = MockNewYorkerDriver()
        articles = pub.get_articles(driver)

        assert len(articles) == 5

    def test_get_articles_urls(self):
        pub = TheNewYorker()
        driver = MockNewYorkerDriver()
        articles = pub.get_articles(driver)

        assert articles == [
            ArticleToScrape(url=url, page_rank=i)
            for i, url in enumerate(
                [
                    "https://www.newyorker.com/magazine/2023/12/04/what-happens-to-a-school-shooters-sister",
                    "https://www.newyorker.com/magazine/2023/12/04/why-trumps-trials-should-be-on-tv",
                    "https://www.newyorker.com/news/our-columnists/should-people-have-the-right-to-say-awful-things-without-facing-legal-consequences",
                    "https://www.newyorker.com/news/daily-comment/at-least-we-can-give-thanks-for-a-tree",
                    "https://www.newyorker.com/news/q-and-a/should-us-aid-to-israel-be-contingent-on-human-rights",
                ],
                start=1,
            )
        ]

    def test_get_article_authors(self):
        """Test get article authors."""
        pub = TheNewYorker()
        driver = MockNewYorkerDriver()
        authors = pub.get_article_authors(driver, "url")
        assert authors == "Jane Mayer"

    def test_get_article_pubdate(self):
        """Test get article pubdate."""
        pub = TheNewYorker()
        driver = MockNewYorkerDriver()
        pubdate = pub.get_article_pubdate(driver, "url")
        assert pubdate == datetime(2024, 2, 29, 18, 30, 37)

    def test_get_article_title(self):
        """Test get article title."""
        pub = TheNewYorker()
        driver = MockNewYorkerDriver()
        title = pub.get_article_title(driver, "url")
        assert title == "The Scandal of Clarence Thomas’s New Clerk"

    def test_get_article_body(self):
        """Test get article body."""
        pub = TheNewYorker()
        driver = MockNewYorkerDriver()
        body = pub.get_article_body(driver, "url")
        for para in [
            "Last week, Supreme Court Justice Clarence Thomas shocked the legal community when the news broke that one of his new law clerks will be Crystal Clanton—who became notorious in 2015 for apparently sending texts that said, “I HATE BLACK PEOPLE. Like fuck them all\xa0.\xa0.\xa0. I hate blacks. End of story.” For most young lawyers, sending such a text would indeed have been the “end of story.” Instead, Clanton is on the cusp of clinching one of the most coveted prizes in the American legal system. In the past several years, as Clanton has risen through the ranks of conservative legal circles, the story of her alleged racist outburst has been curiously transformed into a tale of victimhood. The new narrative is that Clanton was somehow framed by an unnamed enemy who—for motives that remain unclear—fabricated the racist texts to defame her.",
            "Either way, with the help of some rather powerful patrons, and a weak judicial-ethics system, Crystal Clanton is on her way to clerk at the highest court in the land. Eric Segall, a law professor at the Georgia State University College of Law, who served in George H.\xa0W. Bush’s Justice Department, told me, “Can you imagine what would happen if a Black person who said ‘I hate all white people’ ended up clerking for Sotomayor? You’d never hear the end of it on Fox News. But there’s almost total silence about this.”\xa0♦",
        ]:
            assert para in body
