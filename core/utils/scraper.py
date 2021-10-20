import os
from time import sleep
from bbc import get_bbc_links, scrape_bbc_article

import json
from driver import driver_startup


driver = driver_startup()

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


bbc_links = get_bbc_links(driver)
print(bbc_links)
bbc_articles = []

for link in bbc_links:
    article = scrape_bbc_article(link, driver)
    if type(article) == dict:
        bbc_articles.append(article)

with open("bbc.json", "w") as file:
    json.dump(bbc_articles, file, indent=4, default=str)


driver.quit()
