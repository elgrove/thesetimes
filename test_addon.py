from selenium import webdriver

driver = webdriver.Remote(command_executor='127.0.0.1:4444')

driver.get('https://www.ft.com/content/af5cfe1f-e32d-4009-bfa8-b9344d600dc4')

print(driver.title)

driver.quit()