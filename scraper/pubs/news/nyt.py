from bs4 import BeautifulSoup
from datetime import datetime as dt


def get_nyt_links(driver):
    """takes (driver) and returns list of links to scrape"""
    homepage = "https://www.nytimes.com/"
    driver.get(homepage)
    headlines = driver.find_elements_by_class_name("story-wrapper")
    homepage_links = []
    for n in headlines:
        try:
            html = n.get_attribute("outerHTML")
            soup = BeautifulSoup(html, "lxml")
            link = soup.find("a").get("href")
            homepage_links.append(link)
        except:
            pass

    remove_topics = [
        "live",
        "interactive",
        "sports",
        "opinion",
        "podcasts",
        "nyregion",
        "briefing",
        "style",
        "books",
        "newsletters",
        "video",
        "nytdealbookconference",
    ]
    headline_links = []
    for n in homepage_links[:40]:
        if not any(word in n for word in remove_topics):
            if n not in headline_links:
                headline_links.append(n)

    return headline_links


def scrape_nyt_article(link, driver):
    """takes (link, driver) and returns dict of article"""
    driver.get(link)
    page = driver.page_source.encode("utf-8")
    soup = BeautifulSoup(page, "lxml")
    title = str.rstrip(soup.find("meta", property="og:title")["content"])
    pubdate = dt.strptime(
        soup.find("meta", property="article:modified_time")["content"],
        "%Y-%m-%dT%H:%M:%S.%fZ",
    )
    author = soup.find("meta", attrs={"name": "byl"})["content"][3:]
    body = driver.find_element_by_name(
        "articleBody").get_attribute("outerHTML")
    bodysoup = BeautifulSoup(body, "lxml")
    paras = [p.text for p in bodysoup.find_all(
        "p") if p.text != "Advertisement"]

    source = "The New York Times"
    category = "News"
    source_short = 'nyt'

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
