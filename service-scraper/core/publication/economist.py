from datetime import datetime
import re

from core.article_scraper import ArticleToScrape
from core.publication import Publication


class TheEconomist(Publication):
    """Object holding code for scraping the publication The Economist."""

    def __init__(self):
        """Initialise class with required attributes."""
        super().__init__()
        self.name = "The Economist"
        self.short_name = "econ"
        self.category = "News"
        self.homepage = "https://www.economist.com"

    def get_articles(self, driver):
        """Get a list of ArticleToScrape objects."""
        driver.get(self.homepage)
        soup = self.parser(driver.page_source.encode("utf-8"), "lxml")
        top_stories_section = soup.find("section")
        top_stories_anchors = top_stories_section.find_all("a")
        top_stories_urls = [
            self.homepage + a.get("href")
            for a in top_stories_anchors
            if "world-in-brief" not in a.get("href")
        ]
        return [
            ArticleToScrape(url=url, page_rank=i)
            for i, url in enumerate(top_stories_urls, start=1)
        ]

    def get_article_pubdate(self, _driver, article_url):
        """Get article pubdate."""
        date_pattern = r"/(\d{4})/(\d{2})/(\d{2})/"
        match = re.search(date_pattern, article_url)
        year = int(match.group(1))
        month = int(match.group(2))
        day = int(match.group(3))
        return datetime(year, month, day, 5, 0, 0)

    def get_article_body(self, driver, article_url):
        """Get article body."""
        driver.get(article_url)
        soup = self.parser(driver.page_source.encode("utf-8"), "lxml")
        body_section = soup.find("section", attrs={"data-body-id": "cp1"})
        p_tags = body_section.find_all("p")
        paras = [p.text for p in p_tags]
        return paras
