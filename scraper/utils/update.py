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
from pubs.news.dw import get_dw_links, scrape_dw_article
from pubs.news.ft import get_ft_links, scrape_ft_article
from pubs.oped.nyr import get_nyr_links, scrape_nyr_article
from pubs.oped.econ import get_econ_links, scrape_econ_article
from pubs.sports.sky import get_sky_links, scrape_sky_article
from pubs.tech.ars import get_ars_links, scrape_ars_article
from pubs.tech.mit import get_mit_links, scrape_mit_article
from pubs.sports.f365 import get_f365_links, scrape_f365_article


api_url = "http://api:8558/api/"

now = datetime.now().strftime("%Y/%m/%d %H:%M")


def commit_article(article):
    now = datetime.now().strftime("%Y/%m/%d %H:%M")
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
    now = datetime.now().strftime("%Y/%m/%d %H:%M")
    print("Starting web driver")
    driver = driver_startup_headless()
    print("Web driver started")
    print(f"Starting scrape at {now} GMT")

    try:
        print("Scraping FT")
        ft_links = [n for n in get_ft_links(driver)]
        for i, n in enumerate(ft_links, 1):
            print(f"Scraping {n}")
            n_scraped = scrape_ft_article(n, driver)
            if n_scraped:
                n_scraped['pagerank'] = i
            commit_article(n_scraped)
    except:
        print(f'Scrape failed at {now} on FT')

    try:
        print("Scraping NYT")
        nyt_links = [n for n in get_nyt_links(driver)]
        for i, n in enumerate(nyt_links, 1):
            print(f"Scraping {n}")
            n_scraped = scrape_nyt_article(n, driver)
            if n_scraped:
                n_scraped['pagerank'] = i
            commit_article(n_scraped)
    except:
        print(f'Scrape failed at {now} on NYT')

    try:
        print("Scraping BBC")
        bbc_links = [n for n in get_bbc_links(driver)]
        for i, n in enumerate(bbc_links, 1):
            print(f"Scraping {n}")
            n_scraped = scrape_bbc_article(n, driver)
            if n_scraped:
                n_scraped['pagerank'] = i
            commit_article(n_scraped)
    except:
        print(f'Scrape failed at {now} on BBC')

    try:
        print("Scraping WSJ")
        wsj_links = [n for n in get_wsj_links(driver)]
        for i, n in enumerate(wsj_links, 1):
            print(f"Scraping {n}")
            n_scraped = scrape_wsj_article(n, driver)
            if n_scraped:
                n_scraped['pagerank'] = i
            commit_article(n_scraped)
    except:
        print(f'Scrape failed at {now} on WSJ')

    try:
        print("Scraping DW")
        dw_links = [n for n in get_dw_links(driver)]
        for i, n in enumerate(dw_links, 1):
            print(f"Scraping {n}")
            n_scraped = scrape_dw_article(n, driver)
            if n_scraped:
                n_scraped['pagerank'] = i
            commit_article(n_scraped)
    except:
        print(f'Scrape failed at {now} on DW')

    try:
        print("Scraping NYR")
        nyr_links = [n for n in get_nyr_links(driver)]
        for i, n in enumerate(nyr_links, 1):
            print(f"Scraping {n}")
            n_scraped = scrape_nyr_article(n, driver)
            if n_scraped:
                n_scraped['pagerank'] = i
            commit_article(n_scraped)
    except:
        print(f'Scrape failed at {now} on NYR')

    try:
        print("Scraping ECON")
        econ_links = [n for n in get_econ_links(driver)]
        for i, n in enumerate(econ_links, 1):
            print(f"Scraping {n}")
            n_scraped = scrape_econ_article(n, driver)
            if n_scraped:
                n_scraped['pagerank'] = i
            commit_article(n_scraped)
    except:
        print(f'Scrape failed at {now} on ECON')

    try:
        print("Scraping SKY")
        sky_links = [n for n in get_sky_links(driver)]
        for i, n in enumerate(sky_links, 1):
            print(f"Scraping {n}")
            n_scraped = scrape_sky_article(n, driver)
            if n_scraped:
                n_scraped['pagerank'] = i
            commit_article(n_scraped)
    except:
        print(f'Scrape failed at {now} on SKY')

    try:
        print("Scraping F365")
        f365_links = [n for n in get_f365_links(driver)]
        for i, n in enumerate(f365_links, 1):
            print(f"Scraping {n}")
            n_scraped = scrape_f365_article(n, driver)
            if n_scraped:
                n_scraped['pagerank'] = i
            commit_article(n_scraped)
    except:
        print(f'Scrape failed at {now} on F365')

    try:
        print("Scraping ARS")
        ars_links = [n for n in get_ars_links(driver)]
        for i, n in enumerate(ars_links, 1):
            print(f"Scraping {n}")
            n_scraped = scrape_ars_article(n, driver)
            if n_scraped:
                n_scraped['pagerank'] = i
            commit_article(n_scraped)
    except:
        print(f'Scrape failed at {now} on ARS')

    try:
        print("Scraping MIT")
        mit_links = [n for n in get_mit_links(driver)]
        for i, n in enumerate(mit_links, 1):
            print(f"Scraping {n}")
            n_scraped = scrape_mit_article(n, driver)
            if n_scraped:
                n_scraped['pagerank'] = i
            commit_article(n_scraped)
    except:
        print(f'Scrape failed at {now} on MIT')

    now = datetime.now().strftime("%Y/%m/%d %H:%M")
    print(f"Scrape complete at {now}")
    driver.quit()
