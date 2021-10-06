from selenium import webdriver
import os

driver = webdriver.Firefox()

idc = os.path.abspath("ext/i_dont_care_about_cookies-3.3.3-an+fx.xpi")
ubo = os.path.abspath("ext/ublock_origin-1.38.2-an+fx.xpi")
bp = os.path.abspath("ext/bypass-paywalls-firefox.xpi")

ext = [idc, ubo, bp]

for n in ext:
    driver.install_addon(n)

driver.get("https://www.ft.com/content/e06c3b5d-153d-4c86-8c49-0d5447d58e76")

driver.quit()
