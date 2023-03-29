from selenium import webdriver
import os


class WebDriverBuilder:
    def __init__(self):
        self.webdriver_host = "http://webdriver"
        self.webdriver_port = 4444
        self.firefox_options = webdriver.FirefoxOptions()
        self.firefox_options.log.level = "fatal"

    @property
    def extensions(self):
        return [os.path.abspath(f"extensions/{e}") for e in os.listdir("extensions")]

    def install_extensions(self, driver):
        for e in self.extensions:
            webdriver.Firefox.install_addon(driver, e)

    def get_driver(self):
        driver = webdriver.Remote(
            command_executor=f"{self.webdriver_host}:{self.webdriver_port}",
            options=self.firefox_options,
        )
        self.install_extensions(driver)
        driver.get("https://google.com")
        return driver
