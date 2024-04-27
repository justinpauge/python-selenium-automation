from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

# create a new Chrome browser instance
driver_path = ChromeDriverManager().install()
service = Service(driver_path)
driver = webdriver.Chrome(service=Service(driver_path))

# get the path to the ChromeDriver executable
driver_path = ChromeDriverManager().install()

#Open Target website
driver.maximize_window()
driver.implicitly_wait(5)
driver.get('https://www.target.com/')

#Find Links
driver.find_element(By.XPATH, "//*[@data-test='@web/AccountLink']").click()
driver.find_element(By.XPATH, "//*[@data-test='accountNav-signIn']").click()


expected = 'Sign into your Target account'
actual = driver.find_element(By.XPATH, "//h1[contains(@class, 'StyledHeading')]").text
assert expected == actual, f"Expected {expected} did not match actual {actual}"


## MAke sure login is shown
driver.find_element(By.ID,'login')