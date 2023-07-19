from core.article_scraper import ArticleToScrape
from core.publication import Publication


class NewYorkTimes(Publication):
    """Object holding code for scraping the publication Financial Times."""

    def __init__(self):
        """Initialise class with required attributes."""
        super().__init__()
        self.name = "The New York Times"
        self.short_name = "nyt"
        self.category = "New"
        self.homepage = "https://www.nytimes.com"

    @property
    def _filter_exclusion_terms(self):
        """Returns a list of exclusion terms to filter front page articles."""
        return [
            "live",
            "interactive",
            "sports",
            "opinion",
            "podcasts",
            "nyregion",
            "realestate",
            "headway",
            "briefing",
            "style",
            "books",
            "newsletters",
            "video",
            "nytdealbookconference",
            "cooking.nytimes",
        ]

    def get_articles(self, driver):
        """Returns a list of article URLs to be scraped."""
        driver.get(self.homepage)
        soup = self.parser(driver.page_source.encode("utf-8"), "lxml")
        headline_zone = soup.find("div", attrs={"data-hierarchy": "zone"})
        story_sections = headline_zone.find_all(
            "section", attrs={"class": "story-wrapper"}
        )
        story_anchors = [section.find("a") for section in story_sections]
        story_urls = [a.get("href") for a in story_anchors if a is not None]
        filtered_story_urls = [
            a
            for a in story_urls
            if all(word not in a for word in self._filter_exclusion_terms)
        ]
        return [
            ArticleToScrape(url=url, page_rank=i)
            for i, url in enumerate(filtered_story_urls, start=1)
        ]

    def get_article_authors(self, driver, article_url):
        """Get article authors."""
        driver.get(article_url)
        soup = self.parser(driver.page_source.encode("utf-8"), "lxml")
        byline = soup.find("meta", attrs={"name": "byl"}).get("content")
        byline = byline.replace("By", "").strip()
        authors = byline.replace(" and", ",")
        return authors

    def get_article_body(self, driver, article_url):
        """Get article body."""
        driver.get(article_url)
        soup = self.parser(driver.page_source.encode("utf-8"), "lxml")
        body_divs = soup.find_all("div", attrs={"class": "StoryBodyCompanionColumn"})
        body_para_div_results = [t.find_all("p") for t in body_divs]
        body_paras = []
        for result in body_para_div_results:
            for p_tag in result:
                if p_tag.text != "Advertisement":
                    body_paras.append(p_tag.text)
        return body_paras
