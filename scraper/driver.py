from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.firefox_profile import FirefoxProfile
from time import sleep
import os


def driver_startup():
    driver = webdriver.Firefox()

    idc = os.path.abspath(
        "core/utils/ext/i_dont_care_about_cookies-3.3.3-an+fx.xpi")
    ubo = os.path.abspath("core/utils/ext/ublock_origin-1.38.2-an+fx.xpi")
    bp = os.path.abspath("core/utils/ext/bypass-paywalls-firefox.xpi")
    ext = [idc, ubo, bp]

    for n in ext:
        driver.install_addon(n)

    sleep(8)
    return driver


def driver_startup_headless():

    options = Options()
    options.headless = True

    driver = webdriver.Firefox(options=options)

    idc = os.path.abspath(
        "core/utils/ext/i_dont_care_about_cookies-3.3.3-an+fx.xpi")
    ubo = os.path.abspath("core/utils/ext/ublock_origin-1.38.2-an+fx.xpi")
    bp = os.path.abspath("core/utils/ext/bypass-paywalls-firefox.xpi")
    ext = [idc, ubo, bp]

    for n in ext:
        driver.install_addon(n)

    sleep(8)
    return driver

def driver_startup_remote():

    options = Options()
    options.headless = True

    ### how does this bit work??
    fp = FirefoxProfile()
    fp.add_extension('ext/ublock_origin-1.38.2-an+fx.xpi')
    fp.add_extension('ext/i_dont_care_about_cookies-3.3.3-an+fx.xpi')
    fp.add_extension('ext/bypass-paywalls-firefox.xpi')
    driver = webdriver.Remote(command_executor='127.0.0.1:4444', browser_profile=fp)

    idc = os.path.abspath(
        "core/utils/ext/i_dont_care_about_cookies-3.3.3-an+fx.xpi")
    ubo = os.path.abspath("core/utils/ext/ublock_origin-1.38.2-an+fx.xpi")
    bp = os.path.abspath("core/utils/ext/bypass-paywalls-firefox.xpi")
    ext = [idc, ubo, bp]

    for n in ext:
        driver.install_addon(n)

    sleep(8)
    return driver
