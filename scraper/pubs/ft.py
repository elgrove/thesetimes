from bs4 import BeautifulSoup
from datetime import datetime as dt


def get_ft_links(driver):
    """takes (driver) and returns list of links to scrape"""
    # HOMEPAGE
    homepage = "https://www.ft.com"
    driver.get(homepage)
    headlines = driver.find_elements_by_class_name("top-stories")[0].get_attribute(
        "outerHTML"
    )
    headlines = driver.find_elements_by_class_name("top-stories")[0].get_attribute(
        "outerHTML"
    )
    related = driver.find_elements_by_class_name("o-teaser__related")[0].get_attribute(
        "outerHTML"
    )
    headlines = headlines.replace(related, "")
    soup = BeautifulSoup(headlines, "lxml")
    headline_links = [
        link.get("href") for link in soup.findAll("a") if "content" in link.get("href")
    ]
    headline_links = list(dict.fromkeys(headline_links))
    headline_links = [homepage+link for link in headline_links]

    # UK
    uk = 'https://www.ft.com/world/uk'
    driver.get(uk)
    soup = BeautifulSoup(driver.page_source.encode('utf-8'))

    lead = [link.get('href') for link in soup.find(
        'div', attrs={'data-trackable': 'lead-story'}).find_all('a') if 'content' in link.get('href')]

    column = [link.get('href') for link in soup.find(
        'div', attrs={'data-trackable': 'top-stories-column-one'}).find_all('a') if 'content' in link.get('href')]
    uk_links = list(dict.fromkeys(lead+column))
    uk_links = [homepage+link for link in uk_links]

    final = headline_links+uk_links

    return final


def scrape_ft_article(link, driver):
    """takes (link, driver) and returns dict of article"""
    try:
        driver.get(link)
        if "Latest news" not in driver.title:
            page = driver.page_source.encode("utf-8")
            soup = BeautifulSoup(page, "lxml")
            title = str.rstrip(
                soup.find("meta", property="og:title")["content"])
            author = ["FT Staff"]
            if len(soup.findAll("meta", property="article:author")) > 1:
                authors = []
                for n in soup.findAll("meta", property="article:author"):
                    authors.append(n["content"])
                    author = ", ".join(authors)
            else:
                author = soup.find("meta", property="article:author")[
                    "content"]
            pubdate = dt.strptime(
                soup.find("meta", property="article:modified_time")["content"],
                "%Y-%m-%dT%H:%M:%S.%fZ",
            )
            pubdate = pubdate.strftime("%Y-%m-%d %H:%M")
            paras = [
                p.text for p in soup.select("div[class*=content-body]")[0].find_all("p")
            ]
            source = "Financial Times"
            category = "News"
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
    except:
        return None
