import time

from selenium import webdriver
from  selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

a=Options()
a.add_experimental_option("detach",True)
driver=webdriver.Chrome(options=a)

driver.get("https://opensource-demo.orangehrmlive.com/")
print(driver.title)
time.sleep(2)

driver.get("https://www.facebook.com/")
print(driver.title)
time.sleep(2)

driver.back()
print(driver.title)

time.sleep(2)
driver.forward()
print(driver.title)
time.sleep(2)
driver.quit()