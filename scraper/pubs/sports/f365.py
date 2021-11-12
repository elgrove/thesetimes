from bs4 import BeautifulSoup
from datetime import datetime as dt


def get_f365_links(driver):
    driver.get('https://www.football365.com/winners-losers')
    soup = BeautifulSoup(driver.page_source.encode('utf-8'), 'lxml')
    links = [a.get('href') for a in soup.find('section', attrs={
        'class': 'hero'}).find_all('a') if 'premier-league' in a.get('href')]
    return links


def scrape_f365_article(link, driver):
    driver.get(link)
    soup = BeautifulSoup(driver.page_source.encode('utf-8'), 'lxml')

    paras = [p.text for p in soup.find(
        'section', attrs={'class': 'article__body'}).find_all('p') if len(p.text) > 5]

    author = soup.find(
        'meta', attrs={'property': 'article:author'}).get('content')
    pubdate = dt.strptime(
        soup.find('meta', attrs={'name': 'datePublished'}).get('content'), '%Y-%m-%d')
    source = 'Football 365'
    source_short = 'f365'
    title = str.rstrip(
        soup.find("meta", property="og:title")["content"])
    category = 'Sports'

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
