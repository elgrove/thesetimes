from bs4 import BeautifulSoup
from datetime import datetime as dt


def get_bbc_links(driver):
    homepage = "https://www.bbc.co.uk/news/world"
    root = "https://www.bbc.co.uk"
    driver.get(homepage)
    headlines = driver.find_element_by_id(
        "topos-component").get_attribute("outerHTML")
    soup = BeautifulSoup(headlines, "lxml")
    headline_links = [
        link.get("href") for link in soup.findAll("a") if "news" in link.get("href")
    ]
    # remove video links and live text pages
    headline_links = [n for n in headline_links if "/av/" not in n]
    headline_links = [n for n in headline_links if "/live/" not in n]

    headline_links = [root + n for n in headline_links if n[-1].isdigit()]
    headline_links = list(dict.fromkeys(headline_links))
    # trimmed to just top link only
    return headline_links[:1]


def scrape_bbc_article(link, driver):
    driver.get(link)
    soup = BeautifulSoup(driver.page_source.encode("utf-8"), "lxml")
    paras = [p.text for p in soup.find("article").find_all(
        "p", attrs={'class': lambda c: c and 'Paragraph' in c})]
    title = str.rstrip(soup.find("meta", property="og:title")["content"])
    pubdate = dt.strptime(
        soup.find("time")["datetime"],
        "%Y-%m-%dT%H:%M:%S.%fZ",
    )
    author = "BBC Staff"
    source = "BBC News"
    source_short = 'bbc'
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
