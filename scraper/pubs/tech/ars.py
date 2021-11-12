from bs4 import BeautifulSoup
from datetime import datetime as dt


def get_ars_links(driver):
    homepage = "https://www.arstechnica.com"
    driver.get(homepage)
    soup = BeautifulSoup(driver.page_source.encode('utf-8'), 'lxml')
    links = [a.get('href') for a in soup.find('section', attrs={
        'class': 'listing listing-top with-feature'}).find_all('a') if 'author' not in a.get('href')]
    links = list(dict.fromkeys([a for a in links if 'comments' not in a]))

    return links


def scrape_ars_article(link, driver):
    driver.get(link)
    soup = BeautifulSoup(driver.page_source.encode('utf-8'), 'lxml')
    paras = [p.text for p in soup.find(
        'div', attrs={'itemprop': 'articleBody'}).find_all('p') if len(p.text) > 1]
    source = 'Ars Technica'
    source_short = 'ars'
    category = 'Tech'
    title = soup.find('meta', attrs={'property': 'og:title'}).get('content')
    author = soup.find('span', attrs={'itemprop': 'name'}).text
    pubdate = dt.strptime(soup.find('time').get(
        'datetime')[:-6], '%Y-%m-%dT%H:%M:%S')

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
