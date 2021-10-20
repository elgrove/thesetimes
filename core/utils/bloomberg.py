from bs4 import BeautifulSoup
from selenium.webdriver.common.keys import Keys
import lxml
from datetime import datetime as dt
from time import sleep


def get_blb_links(driver):
    """takes (driver) and returns list of links to scrape"""
    homepage = "https://www.bloomberg.com/europe"
    rootpage = "https://www.bloomberg.com"
    driver.get(homepage)
    ssm = driver.find_elements_by_class_name("single-story-module")[0].get_attribute(
        "outerHTML"
    )
    spm_1 = driver.find_elements_by_class_name("story-package-module")[0].get_attribute(
        "outerHTML"
    )
    spm_2 = driver.find_elements_by_class_name("story-package-module")[1].get_attribute(
        "outerHTML"
    )
    oped = driver.find_elements_by_class_name("story-package-module")[2].get_attribute(
        "outerHTML"
    )
    soup = BeautifulSoup(ssm + spm_1 + spm_2 + oped, "lxml")
    links = [
        rootpage + link.get("href")
        for link in soup.findAll("a")
        if "/news/" in link.get("href") or "/opinion/" in link.get("href")
    ]
    links = list(dict.fromkeys(links))
    return links


def scrape_blb_article(link, driver):
    """takes (link, driver) and returns dict of article"""
    driver.get(link)
    # driver.find_element_by_tag_name("body").send_keys(Keys.PAGE_DOWN)
    # driver.find_element_by_tag_name("body").send_keys(Keys.PAGE_DOWN)
    # driver.find_element_by_tag_name("body").send_keys(Keys.PAGE_DOWN)
    # sleep(10)

    if "robot" not in driver.title:
        page = driver.page_source.encode("utf-8")
        soup = BeautifulSoup(page, "lxml")
        title = str.strip(soup.find("meta", property="og:title")["content"])
        author = ["Bloomberg Staff"]
        try:
            if len(soup.findAll("meta", attrs={"name": "parsely-author"})) > 1:
                authors = []
                for n in soup.findAll("meta", attrs={"name": "parsely-author"}):
                    authors.append(n["content"])
                    author = ", ".join(authors)
            else:
                author = soup.find("meta", attrs={"name": "parsely-author"})["content"]
        except:
            pass
        pubdate = dt.strptime(
            soup.find("meta", attrs={"name": "parsely-pub-date"})["content"],
            "%Y-%m-%dT%H:%M:%S.%fZ",
        )
        pubdate = pubdate.strftime("%Y-%m-%d %H:%M")
        body = driver.find_element_by_class_name("middle-column").get_attribute(
            "outerHTML"
        )
        bodysoup = BeautifulSoup(body, "lxml")
        paras = [p.text for p in bodysoup.find_all("p")]
        article = dict(title=title, author=author, pubdate=pubdate, body=paras)
        return article
