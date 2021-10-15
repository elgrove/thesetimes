from selenium import webdriver
import os
from time import sleep
from ft import get_ft_links, scrape_ft_article
import json


def driver_startup():
    driver = webdriver.Firefox()

    idc = os.path.abspath("ext/i_dont_care_about_cookies-3.3.3-an+fx.xpi")
    ubo = os.path.abspath("ext/ublock_origin-1.38.2-an+fx.xpi")
    bp = os.path.abspath("ext/bypass-paywalls-firefox.xpi")
    ext = [idc, ubo, bp]

    for n in ext:
        driver.install_addon(n)

    sleep(8)
    return driver


driver = driver_startup()

ft_links = get_ft_links(driver)
ft_articles = []

for link in ft_links:
    article = scrape_ft_article(link, driver)
    ft_articles.append(article)

with open("ft.json", "w") as file:
    json.dump(ft_articles, file, indent=4, default=str)


driver.quit()
