from bs4 import BeautifulSoup
import lxml
from datetime import datetime as dt


def get_wsj_links(driver):
    homepage = "https://www.wsj.com/"
    driver.get(homepage)

    page = driver.page_source.encode("utf-8")
    soup = BeautifulSoup(page)

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

    return headline_links
