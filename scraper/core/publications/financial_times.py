from datetime import datetime as dt

from core.publications import Publication


class FinancialTimes(Publication):
    def __init__(self):
        super().__init__()
        self.name = "Financial Times"
        self.short_name = "ft"
        self.category = "News"
        self.homepage = "https://www.ft.com"

    def get_articles(self, driver):
        driver.get(self.homepage)
        soup = self.parser(driver.page_source.encode("utf-8"), "lxml")
        article_urls = [
            self.homepage + a.get("href")
            for soup in [
                section.find_all(
                    "a", attrs={"data-trackable-context-story-link": "heading-link"}
                )
                for section in soup.find_all(
                    attrs={"data-trackable-context-list-type": "top-stories"}
                )
                # only top 3 sections
            ][:3]
            for a in soup
            if "content" in a.get("href")
        ]
        return article_urls

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
