from bs4 import BeautifulSoup
from datetime import datetime as dt
from time import sleep


def get_ft_links(driver):
    """takes (driver) and returns list of links to scrape"""
    # HOMEPAGE
    homepage = "https://www.ft.com"
    driver.get(homepage)
    soup = BeautifulSoup(driver.page_source.encode("utf-8"), "lxml")
    headline_links = [
        homepage + a.get("href")
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

    # UK
    uk = "https://www.ft.com/world/uk"
    driver.get(uk)
    soup = BeautifulSoup(driver.page_source.encode("utf-8"), "lxml")

    lead = [
        link.get("href")
        for link in soup.find("div", attrs={"data-trackable": "lead-story"}).find_all(
            "a"
        )
        if "content" in link.get("href")
    ]

    column = [
        link.get("href")
        for link in soup.find(
            "div", attrs={"data-trackable": "top-stories-column-one"}
        ).find_all("a")
        if "content" in link.get("href")
    ]
    uk_links = list(dict.fromkeys(lead + column))
    uk_links = [homepage + link for link in uk_links]

    final = headline_links + uk_links

    return final


def scrape_ft_article(link, driver):
    """takes (link, driver) and returns dict of article"""
    driver.get(link)

    if "live news" not in str.lower(driver.title):
        page = driver.page_source.encode("utf-8")
        soup = BeautifulSoup(page, "lxml")
        title = str.rstrip(soup.find("meta", property="og:title")["content"])
        author = ["FT Staff"]
        if len(soup.findAll("meta", property="article:author")) > 1:
            authors = []
            for n in soup.findAll("meta", property="article:author"):
                authors.append(n["content"])
                author = ", ".join(authors)
        else:
            author = soup.find("meta", property="article:author")["content"]
        pubdate = dt.strptime(
            soup.find("meta", property="article:modified_time")["content"],
            "%Y-%m-%dT%H:%M:%S.%fZ",
        )
        if pubdate.microsecond:
            pubdate = pubdate.replace(microsecond=0)
        paras = [
            p.text for p in soup.select("div[class*=content-body]")[0].find_all("p")
        ]
        source = "Financial Times"
        source_short = "ft"
        category = "News"

        article = dict(
            source=source,
            source_short=source_short,
            url=link,
            category=category,
            title=title,
            author=author,
            pubdate=pubdate,
            body=paras,
        )
        return article
