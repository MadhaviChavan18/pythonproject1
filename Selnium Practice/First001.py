from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

chrome_options = Options()
chrome_options.add_experimental_option("detach",True)
driver = webdriver.Chrome(options=chrome_options)

driver.get("https://opensource-demo.orangehrmlive.com/")
driver.maximize_window()
print(driver.title)

driver.get("https://demoqa.com/")
driver.maximize_window()
print(driver.title)
driver.quit()

