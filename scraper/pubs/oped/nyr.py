from bs4 import BeautifulSoup
from datetime import datetime as dt

from bs4.element import SoupStrainer


def get_nyr_links(driver):
    homepage = "https://www.newyorker.com"
    driver.get(homepage)
    soup = BeautifulSoup(driver.page_source.encode('utf-8'), 'lxml')
    headline_links = list(dict.fromkeys([a.get('href') for a in soup.select(
        "div[class*=SummaryCollageFourWrapper]")[0].find_all('a')]))
    headline_links = [homepage+n for n in headline_links if n.count('/') >= 3]

    return headline_links


def scrape_nyr_article(link, driver):
    driver.get(link)
    soup = driver.page_source.encode('utf-8')
    soup = BeautifulSoup(soup, 'lxml')
    title = str.rstrip(soup.find("meta", property="og:title")["content"])

    bodysoup = driver.find_element_by_class_name(
        'body').get_attribute('outerHTML')
    bodysoup = BeautifulSoup(bodysoup, 'lxml')
    paras = [p.text for p in bodysoup.find_all('p')]

    source = "The New Yorker"
    source_short = 'nyr'
    category = "Opinion"
    author = soup.find('span', attrs={"itemprop": "name"}).text
    # pubdate = dt.now()
    pubdate = dt.strptime(soup.find('time').text, '%B %d, %Y')

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
