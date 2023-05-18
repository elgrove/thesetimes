from datetime import datetime as dt

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

    def get_articles(self, driver):  # TODO could be broken up
        """Returns a list of article URLs to be scraped."""
        driver.get(self.homepage)
        soup = self.parser(driver.page_source.encode("utf-8"), "lxml")

        top_story_divs_to_scrape = 3

        top_stories_divs = soup.find_all(
            attrs={"data-trackable-context-list-type": "top-stories"}
        )[:top_story_divs_to_scrape]

        heading_anchors = []
        for section in top_stories_divs:
            heading_anchors.extend(
                section.find_all(
                    "a", attrs={"data-trackable-context-story-link": "heading-link"}
                )
            )

        article_urls = [
            self.homepage + a.get("href")
            for a in heading_anchors
            if "content" in a.get("href")
        ]

        # filtering out live news feed pages
        live_news_urls = []
        div_containing_live_news = [
            d for d in top_stories_divs if "FT live news" in d.text
        ]
        for div in div_containing_live_news:
            story_group = div.find("div", attrs={"class": "story-group"})
            for a in story_group.find_all("a"):
                if "content" in a.get("href"):
                    live_news_urls.append(self.homepage + a.get("href"))

        article_urls = [a for a in article_urls if a not in live_news_urls]

        return [
            ArticleToScrape(url=url, page_rank=i) for i, url in enumerate(article_urls)
        ]

    def get_article_authors(self, driver, article_url):
        """Returns the author(s) of the article as a string, comma-seperated if more than one."""
        driver.get(article_url)
        soup = self.parser(driver.page_source.encode("utf-8"), "lxml")
        author = "FT Staff"
        if len(soup.findAll("meta", property="article:author")) > 1:
            authors = []
            for n in soup.findAll("meta", property="article:author"):
                authors.append(n["content"])
                author = ", ".join(authors)
        else:
            author = soup.find("meta", property="article:author")["content"]
        return author

    def get_article_pubdate(self, driver, article_url):
        """Returns the article published date as a datetime object."""
        driver.get(article_url)
        soup = self.parser(driver.page_source.encode("utf-8"), "lxml")
        pubdate = dt.strptime(
            soup.find("meta", property="article:modified_time")["content"],
            "%Y-%m-%dT%H:%M:%S.%fZ",
        )
        if pubdate.microsecond:
            pubdate = pubdate.replace(microsecond=0)
        return pubdate

    def get_article_title(self, driver, article_url):
        """Returns the article title as a string."""
        driver.get(article_url)
        soup = self.parser(driver.page_source.encode("utf-8"), "lxml")
        title = str.rstrip(soup.find("meta", property="og:title")["content"])
        return title

    def get_article_body(self, driver, article_url):
        """Returns the article body as a list of strings, one for each paragraph."""
        driver.get(article_url)
        soup = self.parser(driver.page_source.encode("utf-8"), "lxml")
        body = [
            p.text for p in soup.select("div[class*=content-body]")[0].find_all("p")
        ]
        return body