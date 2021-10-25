import os
from time import sleep
from bbc import get_bbc_links, scrape_bbc_article
from driver import driver_startup_headless
from nyt import get_nyt_links, scrape_nyt_article
from dw import get_dw_links, scrape_dw_article
from wsj import get_wsj_links, scrape_wsj_article

import json


driver = driver_startup_headless()

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

wsj_links = get_wsj_links(driver)
wsj_articles = []
for link in wsj_links:
    article = scrape_wsj_article(link, driver)
    if type(article) == dict:
        wsj_articles.append(article)

with open("wsj.json", "w") as file:
    json.dump(wsj_articles, file, indent=4, default=str)


driver.quit()
