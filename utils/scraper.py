from selenium import webdriver
import os
from time import sleep
from ft import scrape_ft


def driver_startup():
    driver = webdriver.Firefox()

    idc = os.path.abspath("../ext/i_dont_care_about_cookies-3.3.3-an+fx.xpi")
    ubo = os.path.abspath("../ext/ublock_origin-1.38.2-an+fx.xpi")
    bp = os.path.abspath("../ext/bypass-paywalls-firefox.xpi")
    ext = [idc, ubo, bp]

    for n in ext:
        driver.install_addon(n)

    sleep(8)
    return driver


driver = driver_startup()

ft = scrape_ft(driver)

print(list(ft.keys()))

driver.quit()
