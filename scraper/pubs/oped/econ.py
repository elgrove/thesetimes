from bs4 import BeautifulSoup
from datetime import datetime as dt
import re


def get_econ_links(driver):
    """takes (driver) and returns list of links to scrape"""
    homepage = "https://www.economist.com"
    driver.get(homepage)
    soup = BeautifulSoup(driver.page_source.encode('utf-8'), 'lxml')

    top_links = [soup.find('a', attrs={'data-analytics': 'top_stories:headline_1'}).get('href'),
                 soup.find(
        'a', attrs={'data-analytics': 'top_stories:headline_2'}).get('href'),
        soup.find('a', attrs={'data-analytics': 'top_stories:headline_3'}).get('href')]

    full_links = [n for n in top_links if n.startswith('http')]
    part_links = [homepage+n for n in top_links if not n.startswith('http')]

    headline_links = full_links + part_links

    return headline_links


def scrape_econ_article(link, driver):
    driver.get(link)
    page = driver.page_source.encode("utf-8")
    soup = BeautifulSoup(page, 'lxml')

    pubdate = dt.now()

    if soup.find('time').get('datetime'):
        pubdate = dt.strptime(
            soup.find('time').get('datetime'),
            "%Y-%m-%dT%H:%M:%SZ",
        )
    else:
        pubdate = str(soup.find('time').get('text'))
        pubdate = re.sub(r'(\d)(st|nd|rd|th)', r'\1', pubdate)
        pubdate = dt.strptime(pubdate, "%b %-d %Y")

    title = str.rstrip(
        soup.find("meta", property="og:title").get("content"))

    bodysoup = driver.find_element_by_class_name(
        'layout-article-body').get_attribute('outerHTML')
    bodysoup = BeautifulSoup(bodysoup, 'lxml')
    paras = [p.text for p in bodysoup.find_all('p')]

    source = "The Economist"
    source_short = 'econ'
    category = "Opinion"
    author = "The Economist"

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
