from datetime import datetime as dt
from functools import cached_property

from core.article_scraper import ArticleToScrape
from core.publication import Publication


class FinancialTimes(Publication):
    """Object holding code for scraping the publication Financial Times."""

    def __init__(self):
        """Initialise class with required attributes."""
        super().__init__()
        self.name = "Financial Times"
        self.short_name = "ft"
        self.category = "News"
        self.homepage = "https://www.ft.com"

    def _get_top_story_divs(self, soup, top_story_divs=3):
        return soup.find_all(attrs={"data-trackable-context-list-type": "top-stories"})[
            :top_story_divs
        ]

    def _get_top_story_urls(self, soup):
        heading_anchors = []
        for section in self._get_top_story_divs(soup):
            heading_anchors.extend(
                section.find_all(
                    "a", attrs={"data-trackable-context-story-link": "heading-link"}
                )
            )

        return [
            self.homepage + a.get("href")
            for a in heading_anchors
            if "content" in a.get("href")
        ]

    def _get_live_news_urls(self, soup):
        live_news_urls = []
        div_containing_live_news = [
            d for d in self._get_top_story_divs(soup) if "FT live news" in d.text
        ]
        for div in div_containing_live_news:
            story_group = div.find("div", attrs={"class": "story-group"})
            for a in story_group.find_all("a"):
                if "content" in a.get("href"):
                    live_news_urls.append(self.homepage + a.get("href"))
        return live_news_urls

    def get_articles(self, driver):
        """Returns a list of article URLs to be scraped."""
        driver.get(self.homepage)
        soup = self.parser(driver.page_source.encode("utf-8"), "lxml")
        top_story_urls = self._get_top_story_urls(soup)
        live_news_urls = self._get_live_news_urls(soup)
        article_urls = [a for a in top_story_urls if a not in live_news_urls]

        return [
            ArticleToScrape(url=url, page_rank=i)
            for i, url in enumerate(article_urls, start=1)
        ]

    def get_article_body(self, driver, article_url):
        """Returns the article body as a list of strings, one for each paragraph."""
        driver.get(article_url)
        soup = self.parser(driver.page_source.encode("utf-8"), "lxml")
        body = [
            p.text for p in soup.select("div[class*=content-body]")[0].find_all("p")
        ]
        return body
