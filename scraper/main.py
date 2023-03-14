from selenium import webdriver


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
driver = webdriver.Remote(
    command_executor="http://browser:4444", options=firefox_options
)
driver.get("http://www.google.com")
print(driver.page_source)
driver.quit()
