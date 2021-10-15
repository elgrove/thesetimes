from bs4 import BeautifulSoup
import lxml


def scrape_ft(driver):
    homepage = "https://www.ft.com/"
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
    headline_links = [homepage[:-1] + link for link in headline_links]

    ft = {}
    for link in headline_links:
        driver.get(link)
        if "Latest news" not in driver.title:
            page = driver.page_source.encode("utf-8")
            soup = BeautifulSoup(page, "lxml")
            title = str.strip(driver.title.split("|")[0])
            paras = [
                p.text for p in soup.select("div[class*=content-body]")[0].find_all("p")
            ]
            ft[title] = paras

    return ft
