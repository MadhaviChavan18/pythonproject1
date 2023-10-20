import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select
ob=Options()
ob.add_experimental_option("detach",True)
driver=webdriver.Chrome(options=ob)

driver.get("https://rahulshettyacademy.com/")
driver.maximize_window()
time.sleep(5)
driver.close()