from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.firefox_profile import FirefoxProfile
from time import sleep
import os


def driver_startup_headless():
    options = Options()
    options.headless = True

    driver = webdriver.Firefox(
        options=options, firefox_binary="/opt/firefox/firefox-bin"
    )

    ext = [
        os.path.abspath(f"extensions/{e}")
        for e in os.listdir("extensions")
        if e.endswith(".xpi")
    ]

    for n in ext:
        driver.install_addon(n)

    sleep(8)
    return driver


if __name__ == "__main__":
    driver = driver_startup_headless()
    driver.get("https://www.ft.com/content/5e444ba2-0afc-49e8-bfec-5fc17ef7ee39")
    print(driver.page_source)
