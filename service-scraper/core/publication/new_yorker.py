from core.article_scraper import ArticleToScrape
from core.publication import Publication


class TheNewYorker(Publication):
    """Object holding code for scraping the publication The New Yorker."""

    def __init__(self):
        """Initialise class with required attributes."""
        super().__init__()
        self.name = "The New Yorker"
        self.short_name = "nyr"
        self.category = "Opinion"
        self.homepage = "https://www.newyorker.com"

    def get_articles(self, driver):
        """Returns a list of article URLs to be scraped."""
        driver.get(self.homepage)
        soup = self.parser(driver.page_source.encode("utf-8"), "lxml")
        top_nine_collage_div = soup.find("div", id="news-&amp;-culture")
        top_nine_collage_urls = list(
            dict.fromkeys(  # dedupe list, preserving order
                [
                    self.homepage + a.get("href")
                    for a in top_nine_collage_div.find_all(
                        "a", attrs={"data-recirc-pattern": "summary-item"}
                    )
                ]
            )
        )

        return [
            ArticleToScrape(url=url, page_rank=i)
            for i, url in enumerate(top_nine_collage_urls, start=1)
        ]

    def get_article_body(self, driver, article_url):
        """Returns the article body as a list of strings, one for each paragraph."""
        driver.get(article_url)
        soup = self.parser(driver.page_source.encode("utf-8"), "lxml")
        body_div = soup.find("div", attrs={"data-testid": "BodyWrapper"})
        first_para = [
            p.text for p in body_div.find_all("p", attrs={"class": "has-dropcap"})
        ]
        rest_paras = [
            p.text for p in body_div.find_all("p", attrs={"class": "paywall"})
        ]

        return first_para + rest_paras
