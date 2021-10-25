from bs4 import BeautifulSoup
import lxml
from datetime import datetime as dt


def get_wsj_links(driver):
    homepage = "https://www.wsj.com/"
    driver.get(homepage)

    page = driver.page_source.encode("utf-8")
    soup = BeautifulSoup(page, "lxml")

    topnews = str(soup.find("div", attrs={"aria-label": "Top News"}))
    related = [
        str(n)
        for n in soup.find("div", attrs={"aria-label": "Top News"}).find_all("ul")
    ]

    for n in related:
        topnews = topnews.replace(n, "")

    headline_links = [
        link.get("href").split("?")[0]
        for link in BeautifulSoup(topnews, "lxml").find_all("a")
        if "articles" in link.get("href")
    ]

    headline_links = list(dict.fromkeys(headline_links))

    for n in headline_links:
        if "/amp/" in n:
            n.replace("/amp/", "/")

    return headline_links


def scrape_wsj_article(link, driver):
    driver.get(link)
    page = driver.page_source.encode("utf-8")
    soup = BeautifulSoup(page, "lxml")
    author = soup.find("meta", attrs={"name": "author"}).get("content")
    title = soup.find("meta", attrs={"name": "article.headline"}).get("content")

    pubdate = dt.strptime(
        soup.find("meta", attrs={"name": "article.published"}).get("content"),
        "%Y-%m-%dT%H:%M:%S.%fZ",
    )

    bodysoup = soup.find("article")

    paras = [p.text for p in bodysoup.find_all("p") if "Copyright" not in p.text]
    paras = [
        n.replace("\n", "").replace("    ", " ") for n in paras if "@wsj.com" not in n
    ]

    article = dict(title=title, author=author, pubdate=pubdate, body=paras)
    return article
