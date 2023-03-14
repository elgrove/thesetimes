from selenium import webdriver
import os


def wait_for_service(service_url, timeout):
    import socket
    import time

    host, port = service_url.split(":")
    timeout_time = time.time() + timeout

    while True:
        if time.time() > timeout_time:
            raise TimeoutError(
                f"Timed out waiting for {service_url} to become available"
            )

        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(1)
            sock.connect((host, int(port)))
            sock.shutdown(socket.SHUT_RDWR)
            return True

        except (ConnectionRefusedError, socket.timeout):
            time.sleep(1)
            continue

        finally:
            sock.close()


wait_for_service("browser:4444", timeout=60)
firefox_options = webdriver.FirefoxOptions()

extensions = [os.path.abspath(f"extensions/{e}") for e in os.listdir("extensions")]


driver = webdriver.Remote(
    command_executor="http://browser:4444", options=firefox_options
)

for e in extensions:
    webdriver.Firefox.install_addon(driver, e)

driver.get("https://www.ft.com/content/e351ccfd-641f-4203-b778-19d656b8543b")
print(driver.page_source)
driver.quit()
