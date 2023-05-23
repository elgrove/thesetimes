import os

from selenium import webdriver


class WebDriverBuilder:
    """Class for building Selenium webdriver instances."""

    def __init__(self):
        """Initialise."""
        self.webdriver_host = "http://webdriver"
        self.webdriver_port = 4444
        self.firefox_options = webdriver.FirefoxOptions()
        self.firefox_options.log.level = "fatal"

    @property
    def extensions(self):
        """Returns a list of file paths at which Firefox extensions lie."""
        return [
            os.path.abspath(f"extensions/{ext}") for ext in os.listdir("extensions")
        ]

    def install_extensions(self, driver):
        """Install Firefox extensions."""
        for e in self.extensions:
            webdriver.Firefox.install_addon(driver, e)

    def get_driver(self):
        """Returns a webdriver instance with extensions installed."""
        driver = webdriver.Remote(
            command_executor=f"{self.webdriver_host}:{self.webdriver_port}",
            options=self.firefox_options,
        )
        self.install_extensions(driver)
        driver.get("https://google.com")
        return driver
