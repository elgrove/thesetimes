from bs4 import BeautifulSoup
from datetime import datetime as dt


def get_mit_links(driver):
    homepage = "https://www.technologyreview.com/"
    driver.get(homepage)
    soup = BeautifulSoup(driver.page_source.encode('utf-8'), 'lxml')
    links = [li.find('a') for li in soup.find_all('h3')] + \
        [li.find('a') for li in soup.find_all('h1')]
    links = [l for l in links if l != None]
    links = [l.get('href') for l in links]
    # remove podcast stories
    links = [l for l in links if 'i-was-there-when' not in l]
    popular = [a.get('href') for a in soup.select_one(
        "ol[class*=popular--inFeed__stories]").find_all('a') if 'author' not in a.get('href')]
    headline_links = links[:5] + popular

    return headline_links


def scrape_mit_article(link, driver):
    driver.get(link)
    soup = BeautifulSoup(driver.page_source.encode('utf-8'), 'lxml')

    paras = []
    for n in soup.find_all('div', attrs={'class': lambda divclass: divclass and divclass.startswith('gutenbergContent')}):
        ps = n.find_all('p')
        pg = [p.text for p in ps]
        for p in pg:
            paras.append(p)

    source = 'MIT Technology Review'
    category = 'Tech'
    title = str.rstrip(soup.find("meta", property="og:title")["content"])
    datestr = link[link.find('20'):link.find('20')+10]
    pubdate = dt.strptime(datestr, '%Y/%m/%d')
    author = soup.find('a', attrs={
        'class': lambda divclass: divclass and divclass.startswith('byline__name')
    }).text.replace('archive page', '')

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
