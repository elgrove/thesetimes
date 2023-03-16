from selenium import webdriver
import os

import socket
import time


class WebDriverBuilder:
    def __init__(self):
        self.webdriver_host = "http://webdriver"
        self.webdriver_port = 4444
        self.firefox_options = webdriver.FirefoxOptions()

    @property
    def extensions(self):
        return [os.path.abspath(f"extensions/{e}") for e in os.listdir("extensions")]

    def install_extensions(self, driver):
        for e in self.extensions:
            webdriver.Firefox.install_addon(driver, e)

    def wait_for_webdriver_service(self):
        timeout_time = time.time() + 60
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        while True:
            if time.time() > timeout_time:
                raise TimeoutError(
                    f"Timed out waiting for webdriver service to become available"
                )

            try:
                sock.settimeout(1)
                sock.connect((self.webdriver_host, int(self.webdriver_port)))
                sock.shutdown(socket.SHUT_RDWR)
                return True

            except (ConnectionRefusedError, socket.timeout):
                time.sleep(1)
                continue

            finally:
                sock.close()

    def get_driver(self):
        self.wait_for_webdriver_service()
        driver = webdriver.Remote(
            command_executor=f"{self.webdriver_host}:{self.webdriver_port}",
            options=self.firefox_options,
        )
        self.install_extensions(driver)
        driver.get("https://google.com")
        return driver
