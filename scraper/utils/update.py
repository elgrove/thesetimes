import os
from time import sleep
from datetime import datetime
from utils.driver import driver_startup_headless
import json
import requests
from pymongo import MongoClient
from pubs.news.nyt import get_nyt_links, scrape_nyt_article
from pubs.news.bbc import get_bbc_links, scrape_bbc_article
from pubs.news.wsj import get_wsj_links, scrape_wsj_article
from pubs.news.bloomberg import get_blb_links, scrape_blb_article
from pubs.news.dw import get_dw_links, scrape_dw_article
from pubs.news.ft import get_ft_links, scrape_ft_article
from pubs.oped.nyr import get_nyr_links, scrape_nyr_article
from pubs.oped.econ import get_econ_links, scrape_econ_article
from pubs.sports.sky import get_sky_links, scrape_sky_article
from pubs.tech.ars import get_ars_links, scrape_ars_article
from pubs.tech.mit import get_mit_links, scrape_mit_article


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

    try:
        print("Scraping FT")
        ft_links = [n for n in get_ft_links(driver)]
        for n in ft_links:
            print(f"Scraping {n}")
            n_scraped = scrape_ft_article(n, driver)
            commit_article(n_scraped)
    except:
        print(f'Scrape failed at {now} on FT')

    try:
        print("Scraping NYT")
        nyt_links = [n for n in get_nyt_links(driver)]
        for n in nyt_links:
            print(f"Scraping {n}")
            n_scraped = scrape_nyt_article(n, driver)
            commit_article(n_scraped)
    except:
        print(f'Scrape failed at {now} on NYT')

    try:
        print("Scraping BBC")
        bbc_links = [n for n in get_bbc_links(driver)]
        for n in bbc_links:
            print(f"Scraping {n}")
            n_scraped = scrape_bbc_article(n, driver)
            commit_article(n_scraped)
    except:
        print(f'Scrape failed at {now} on BBC')

    try:
        print("Scraping WSJ")
        wsj_links = [n for n in get_wsj_links(driver)]
        for n in wsj_links[:3]:
            print(f"Scraping {n}")
            n_scraped = scrape_wsj_article(n, driver)
            commit_article(n_scraped)
    except:
        print(f'Scrape failed at {now} on WSJ')

    try:
        print("Scraping DW")
        dw_links = [n for n in get_dw_links(driver)]
        for n in dw_links:
            print(f"Scraping {n}")
            n_scraped = scrape_dw_article(n, driver)
            commit_article(n_scraped)
    except:
        print(f'Scrape failed at {now} on DW')

    try:
        print("Scraping New Yorker")
        nyr_links = [n for n in get_nyr_links(driver)]
        for n in nyr_links:
            print(f"Scraping {n}")
            n_scraped = scrape_nyr_article(n, driver)
            commit_article(n_scraped)
    except:
        print(f'Scrape failed at {now} on New Yorker')

    try:
        print("Scraping Economist")
        econ_links = [n for n in get_econ_links(driver)]
        for n in econ_links:
            print(f"Scraping {n}")
            n_scraped = scrape_econ_article(n, driver)
            commit_article(n_scraped)
    except:
        print(f'Scrape failed at {now} on Economist')

    try:
        print("Scraping Sky Sports")
        sky_links = [n for n in get_sky_links(driver)]
        for n in sky_links:
            print(f"Scraping {n}")
            n_scraped = scrape_sky_article(n, driver)
            commit_article(n_scraped)
    except:
        print(f'Scrape failed at {now} on Sky Sports')

    try:
        print("Scraping Ars Technica")
        ars_links = [n for n in get_ars_links(driver)]
        for n in ars_links:
            print(f"Scraping {n}")
            n_scraped = scrape_ars_article(n, driver)
            commit_article(n_scraped)
    except:
        print(f'Scrape failed at {now} on Ars Technica')

    try:
        print("Scraping MIT Tech Review")
        mit_links = [n for n in get_mit_links(driver)]
        print(mit_links)
        for n in mit_links:
            print(f"Scraping {n}")
            n_scraped = scrape_mit_article(n, driver)
            commit_article(n_scraped)
    except:
        print(f'Scrape failed at {now} on MIT Tech Review')

    print(f"Scrape complete at {now}")
    driver.quit()
