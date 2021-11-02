import os
from time import sleep
from datetime import datetime
from utils.driver import driver_startup_headless
import json
import requests
from pymongo import MongoClient
from pubs.nyt import get_nyt_links, scrape_nyt_article
from pubs.bbc import get_bbc_links, scrape_bbc_article
from pubs.wsj import get_wsj_links, scrape_wsj_article
from pubs.bloomberg import get_blb_links, scrape_blb_article
from pubs.dw import get_dw_links, scrape_dw_article
from pubs.ft import get_ft_links, scrape_ft_article
from pubs.nyr import get_nyr_links, scrape_nyr_article
from pubs.econ import get_econ_links, scrape_econ_article

api_url = "http://api:8558/api/"

now = datetime.now().strftime("%Y/%m/%d %H:%M")

################
# NEEDS REFACTORING BADLY
################


def commit_article(article):
    if type(article) == dict:
        if (
            requests.get(
                api_url + "find/",
                params={"title": article["title"]},
            ).status_code
            == 404
        ):
            requests.post(api_url, json.dumps(article, indent=4, default=str))
            print("Article posted")
        else:
            print("Article already present")


def update_db():
    print("Starting web driver")
    driver = driver_startup_headless()
    print("Web driver started")
    print(f"Starting scrape at {now} GMT")

    print("Scraping FT")
    ft_links = [n for n in get_ft_links(driver)]
    for n in ft_links:
        print(f"Scraping {n}")
        n_scraped = scrape_ft_article(n, driver)
        commit_article(n_scraped)

    print("Scraping NYT")
    nyt_links = [n for n in get_nyt_links(driver)]
    for n in nyt_links:
        print(f"Scraping {n}")
        n_scraped = scrape_nyt_article(n, driver)
        commit_article(n_scraped)

    print("Scraping BBC")
    bbc_links = [n for n in get_bbc_links(driver)]
    for n in bbc_links:
        print(f"Scraping {n}")
        n_scraped = scrape_bbc_article(n, driver)
        commit_article(n_scraped)

    print("Scraping WSJ")
    wsj_links = [n for n in get_wsj_links(driver)]
    for n in wsj_links:
        print(f"Scraping {n}")
        n_scraped = scrape_wsj_article(n, driver)
        commit_article(n_scraped)

    # print("Scraping Bloomberg")
    # blb_links = [n for n in get_blb_links(driver)]
    # for n in blb_links:
    #     print(f"Scraping {n}")
    #     n_scraped = scrape_blb_article(n, driver)
    #     commit_article(n_scraped)

    print("Scraping DW")
    dw_links = [n for n in get_dw_links(driver)]
    for n in dw_links:
        print(f"Scraping {n}")
        n_scraped = scrape_dw_article(n, driver)
        commit_article(n_scraped)

    print("Scraping New Yorker")
    nyr_links = [n for n in get_nyr_links(driver)]
    for n in nyr_links:
        print(f"Scraping {n}")
        n_scraped = scrape_nyr_article(n, driver)
        commit_article(n_scraped)

    print("Scraping Economist")
    econ_links = [n for n in get_econ_links(driver)]
    for n in econ_links:
        print(f"Scraping {n}")
        n_scraped = scrape_econ_article(n, driver)
        commit_article(n_scraped)

    print("Done")
    driver.quit()
