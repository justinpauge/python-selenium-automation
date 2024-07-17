from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

# get the path to the ChromeDriver executable
driver_path = ChromeDriverManager().install()

# create a new Chrome browser instance
service = Service(driver_path)
driver = webdriver.Chrome(service=service)
driver.maximize_window()

sleep(5)

# open the url
driver.get('https://www.amazon.com/')

sleep(10)

# #Find By ID
driver.find_element(By.ID, value= 'twotabsearchtextbox')
#
sleep(5)
#
# #By XPATH
driver.find_element(By.XPATH, value='//input[@placeholder="Search Amazon"]')
#
sleep(5)
#
#By Text
driver.find_element(By.XPATH, value='//a[text()="Best Sellers"]')






print('hi! '*4)

#
#
# print('hi')
#
# # populate search field
# search = driver.find_element(By.NAME, 'q')
# search.clear()
# search.send_keys('Car')
#
# # wait for 4 sec
# sleep(4)
#
# # click search button
# driver.find_element(By.NAME, 'btnK').click()
#
# # verify search results
# assert 'car' in driver.current_url.lower(), f"Expected query not in {driver.current_url.lower()}"
# print('Test Passed')
#
# driver.quit()
