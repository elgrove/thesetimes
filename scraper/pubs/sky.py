from bs4 import BeautifulSoup
from datetime import datetime as dt


def get_sky_links(driver):
    homepage = 'https://www.skysports.com/premier-league-news'
    root = "https://www.skysports.com"
    driver.get(homepage)
    soup = BeautifulSoup(driver.page_source.encode('utf-8'), 'lxml')
    links = [a.get('href') for a in soup.find('div', attrs={
        'class': 'news-list block'}).find_all('a') if '/news/1' in a.get('href')]
    links = list(dict.fromkeys(links))
    links = links[:6]
    return links


def scrape_sky_article(link, driver):
    driver.get(link)
    soup = BeautifulSoup(driver.page_source.encode("utf-8"), "lxml")
    bodysoup = BeautifulSoup(
        str(soup.find('div', attrs={'data-component-name': 'sdc-article-body'})), 'lxml')
    list_links = bodysoup.find_all('ul')
    bodysoup = str(bodysoup)
    for n in list_links:
        bodysoup.replace(str(n), '')
    bodysoup = bodysoup.replace(
        'Please use Chrome browser for a more accessible video player', '')
    paras = [p.text for p in BeautifulSoup(
        bodysoup, 'lxml').find_all('p') if len(p.text) > 0]
    title = soup.find('meta', attrs={'property': 'og:title'}).get('content')
    author = 'Sky Sports'
    pubdate = dt.now()
    pubdate = dt.strptime(soup.find('div', attrs={
                          'class': 'sdc-article-date'}).find('p').text, '%A %d %B %Y %H:%M, UK')
    source = 'Sky Sports'
    category = 'Sports'

    article = dict(
        source=source,
        url=link,
        category=category,
        title=title,
        author=author,
        pubdate=pubdate,
        body=paras,
    )
    return article
