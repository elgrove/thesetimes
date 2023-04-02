from datetime import datetime as dt

from core.publications import Publication


class FinancialTimes(Publication):
    """Object holding code for scraping the publication Financial Times."""

    def __init__(self):
        super().__init__()
        self.name = "Financial Times"
        self.short_name = "ft"
        self.category = "News"
        self.homepage = "https://www.ft.com"

    def get_articles(self, driver):
        driver.get(self.homepage)
        soup = self.parser(driver.page_source.encode("utf-8"), "lxml")

        top_story_divs_to_scrape = 3

        top_stories_divs = soup.find_all(
            attrs={"data-trackable-context-list-type": "top-stories"}
        )[:top_story_divs_to_scrape]

        # filtering out live news feed pages
        live_news_urls = set()
        div_containing_live_news = [
            d for d in top_stories_divs if "FT live news" in d.text
        ]
        for div in div_containing_live_news:
            story_group_live_news = div.find("div", attrs={"class": "story-group"})
            live_news_urls.add(
                {
                    self.homepage + a.get("href")
                    for a in story_group_live_news.find_all("a")
                    if "content" in a.get("href")
                }
            )

        heading_anchors = [
            section.find_all(
                "a", attrs={"data-trackable-context-story-link": "heading-link"}
            )
            for section in top_stories_divs
        ]
        # flatten list of lists
        heading_anchors = [item for sublist in heading_anchors for item in sublist]

        article_urls = {
            self.homepage + a.get("href")
            for a in heading_anchors
            if "content" in a.get("href")
        }

        return list(article_urls - live_news_urls)

    def get_article_authors(self, driver, article_url):
        driver.get(article_url)
        soup = self.parser(driver.page_source.encode("utf-8"), "lxml")
        author = ["FT Staff"]
        if len(soup.findAll("meta", property="article:author")) > 1:
            authors = []
            for n in soup.findAll("meta", property="article:author"):
                authors.append(n["content"])
                author = ", ".join(authors)
        else:
            author = soup.find("meta", property="article:author")["content"]
        return author

    def get_article_pubdate(self, driver, article_url):
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
        driver.get(article_url)
        soup = self.parser(driver.page_source.encode("utf-8"), "lxml")
        title = str.rstrip(soup.find("meta", property="og:title")["content"])
        return title

    def get_article_body(self, driver, article_url):
        driver.get(article_url)
        soup = self.parser(driver.page_source.encode("utf-8"), "lxml")
        body = [
            p.text for p in soup.select("div[class*=content-body]")[0].find_all("p")
        ]
        return body
