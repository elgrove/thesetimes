from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from time import sleep
import os


def driver_startup():
    driver = webdriver.Firefox()

    idc = os.path.abspath("utils/ext/i_dont_care_about_cookies-3.3.3-an+fx.xpi")
    ubo = os.path.abspath("utils/ext/ublock_origin-1.38.2-an+fx.xpi")
    bp = os.path.abspath("utils/ext/bypass-paywalls-firefox.xpi")
    ext = [idc, ubo, bp]

    for n in ext:
        driver.install_addon(n)

    sleep(8)
    return driver


def driver_startup_headless():

    options = Options
    options.headless = True

    driver = webdriver.Firefox(options=options)

    idc = os.path.abspath("utils/ext/i_dont_care_about_cookies-3.3.3-an+fx.xpi")
    ubo = os.path.abspath("utils/ext/ublock_origin-1.38.2-an+fx.xpi")
    bp = os.path.abspath("utils/ext/bypass-paywalls-firefox.xpi")
    ext = [idc, ubo, bp]

    for n in ext:
        driver.install_addon(n)

    sleep(8)
    return driver
