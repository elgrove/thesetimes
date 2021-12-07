from bs4 import BeautifulSoup
from datetime import datetime as dt


def get_dw_links(driver):
    homepage = "https://dw.com/en/top-stories/world/s-1429"
    root = "https://dw.com"
    driver.get(homepage)
    headline_links = []
    for n in [
        n.get_attribute("outerHTML") for n in driver.find_elements_by_class_name("col2")
    ]:
        soup = BeautifulSoup(n, "lxml")
        a = soup.findAll("a")
        for i in a:
            if "overlay" not in i.get("href"):
                headline_links.append(root + i.get("href"))
    headline_links = headline_links[:4]
    return headline_links


def scrape_dw_article(link, driver):
    driver.get(link)
    page = driver.page_source.encode("utf-8")
    soup = BeautifulSoup(page, "lxml")
    title = str.rstrip(soup.find("meta", property="og:title")["content"].split("|")[0])
    author = "DW Staff"
    pubdate = str.strip(soup.find("meta", property="og:title")["content"].split("|")[2])
    # pubdate = dt.now()
    pubdate = dt.strptime(pubdate, "%d.%m.%Y")
    paras = [
        p.text
        for p in soup.find("div", attrs={"class": "longText"}).findAll("p")
        if not "/rc" in p.text
    ]
    article = dict(title=title, author=author, pubdate=pubdate, body=paras)
    source = "Deutsche Welle"
    category = "News"
    source_short = "dw"

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
