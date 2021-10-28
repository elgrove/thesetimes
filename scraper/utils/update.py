import os
from time import sleep
from utils.driver import driver_startup_headless
import json
from pymongo import MongoClient
from pubs.nyt import get_nyt_links, scrape_nyt_article
from pubs.bbc import get_bbc_links, scrape_bbc_article
from pubs.wsj import get_wsj_links, scrape_wsj_article
from pubs.bloomberg import get_blb_links, scrape_blb_article
from pubs.dw import get_dw_links, scrape_dw_article
from pubs.ft import get_ft_links, scrape_ft_article


def update_db():
    print("Starting web driver")
    driver = driver_startup_headless()
    print("Web driver started")

    print("Init MongoDB")
    # mongodb the second one = name of the container
    db_client = MongoClient("mongodb://mongodb:27017/")
    db = db_client["db"]
    collection = db["articles"]
    print("MongoDB Init")

    print(db_client.list_database_names())

    scraped_articles = []

    print("Scraping NYT")
    nyt_links = [n for n in get_nyt_links(driver)]
    for n in nyt_links:
        print(f"Scraping {n}")
        scraped_articles.append(scrape_nyt_article(n, driver))

    print("Scraping BBC")
    bbc_links = [n for n in get_bbc_links(driver)]
    for n in bbc_links:
        print(f"Scraping {n}")
        scraped_articles.append(scrape_bbc_article(n, driver))

    print("Scraping WSJ")
    wsj_links = [n for n in get_wsj_links(driver)]
    for n in wsj_links:
        print(f"Scraping {n}")
        scraped_articles.append(scrape_wsj_article(n, driver))

    print("Scraping Bloomberg")
    blb_links = [n for n in get_blb_links(driver)]
    for n in blb_links:
        print(f"Scraping {n}")
        scraped_articles.append(scrape_blb_article(n, driver))

    print("Scraping DW")
    dw_links = [n for n in get_dw_links(driver)]
    for n in dw_links:
        print(f"Scraping {n}")
        scraped_articles.append(scrape_dw_article(n, driver))

    print("Scraping FT")
    ft_links = [n for n in get_ft_links(driver)]
    for n in ft_links:
        print(f"Scraping {n}")
        scraped_articles.append(scrape_ft_article(n, driver))

    # print("Dumping JSON")
    # with open("test.json", "w") as file:
    #     json.dump(scraped_articles, file, indent=4, default=str)
    print("Writing to MongoDB")
    print(f"{len(scraped_articles)} articles to commit")
    for n in scraped_articles:
        if n:
            # check article is already in the db
            # this could be better, esp using published date instead of modified date
            # but then this would stop me getting updated on developing stories
            # maybe some sort of text diff match threshold? even as much as 20% should catch it
            if not collection.find_one(
                {"source": n["source"], "title": n["title"], "author": n["author"]}
            ):
                collection.insert_one(n)
    print("Done")
    db_client.close()
    driver.quit()
