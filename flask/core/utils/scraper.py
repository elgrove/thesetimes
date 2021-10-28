import os
from time import sleep
from driver import driver_startup_headless
import json
from pymongo import MongoClient
from pubs.nyt import get_nyt_links, scrape_nyt_article
from pubs.bbc import get_bbc_links, scrape_bbc_article
from pubs.wsj import get_wsj_links, scrape_wsj_article
from pubs.bloomberg import get_blb_links, scrape_blb_article
from pubs.dw import get_dw_links, scrape_dw_article
from pubs.ft import get_ft_links, scrape_ft_article

print('Starting web driver')
driver = driver_startup_headless()
print('Web driver started')

print('Init MongoDB')
db_client = MongoClient('mongodb://localhost:27017/')
db = db_client['db']
collection = db['articles']
print('MongoDB Init')

scraped_articles = []

print('Scraping NYT')
nyt_links = [n for n in get_nyt_links(driver)]
for n in nyt_links:
    print(f'Scraping {n}')
    scraped_articles.append(scrape_nyt_article(n, driver))

print('Scraping BBC')
bbc_links = [n for n in get_bbc_links(driver)]
for n in bbc_links:
    print(f'Scraping {n}')
    scraped_articles.append(scrape_bbc_article(n, driver))

print('Scraping WSJ')
wsj_links = [n for n in get_wsj_links(driver)]
for n in wsj_links:
    print(f'Scraping {n}')
    scraped_articles.append(scrape_wsj_article(n, driver))

# print('Scraping Bloomberg')
# blb_links = [n for n in get_blb_links(driver)]
# for n in blb_links:
#     print(f'Scraping {n}')
#     scraped_articles.append(scrape_blb_article(n, driver))

print('Scraping DW')
dw_links = [n for n in get_dw_links(driver)]
for n in dw_links:
    print(f'Scraping {n}')
    scraped_articles.append(scrape_dw_article(n, driver))

print('Scraping FT')
ft_links = [n for n in get_ft_links(driver)]
for n in ft_links:
    print(f'Scraping {n}')
    scraped_articles.append(scrape_ft_article(n, driver))

print('Dumping JSON')
with open("test.json", "w") as file:
    json.dump(scraped_articles, file, indent=4, default=str)

for n in scraped_articles:
    if not collection.find_one({'source': n['source'], 'title': n['title']}):
        collection.insert_one(n)

db_client.close()
driver.quit()


# ft_links = get_ft_links(driver)
# ft_articles = []

# for link in ft_links:
#     article = scrape_ft_article(link, driver)
#     ft_articles.append(article)

# with open("ft.json", "w") as file:
#     json.dump(ft_articles, file, indent=4, default=str)

#####################

# blb_links = get_blb_links(driver)
# blb_articles = []

# for link in blb_links:
#     article = scrape_blb_article(link, driver)
#     if type(article) == dict:
#         blb_articles.append(article)

# with open("blb.json", "w") as file:
#     json.dump(blb_articles, file, indent=4, default=str)

#####################


# bbc_links = get_bbc_links(driver)
# bbc_articles = []

# for link in bbc_links:
#     article = scrape_bbc_article(link, driver)
#     if type(article) == dict:
#         bbc_articles.append(article)

# with open("bbc.json", "w") as file:
#     json.dump(bbc_articles, file, indent=4, default=str)

####################

# nyt_links = get_nyt_links(driver)
# nyt_articles = []
# for link in nyt_links:
#     article = scrape_nyt_article(link, driver)
#     if type(article) == dict:
#         nyt_articles.append(article)

# with open("nyt.json", "w") as file:
#     json.dump(nyt_articles, file, indent=4, default=str)


####################

# dw_links = get_dw_links(driver)
# dw_articles = []
# for link in dw_links:
#     article = scrape_dw_article(link, driver)
#     if type(article) == dict:
#         dw_articles.append(article)

# with open("dw.json", "w") as file:
#     json.dump(dw_articles, file, indent=4, default=str)

#####################

# wsj_links = get_wsj_links(driver)
# wsj_articles = []
# for link in wsj_links:
#     article = scrape_wsj_article(link, driver)
#     if type(article) == dict:
#         wsj_articles.append(article)
