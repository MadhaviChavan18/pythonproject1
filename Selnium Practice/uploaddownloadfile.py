import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver import ActionChains
u=Options()
u.add_experimental_option("detach",True)
driver=webdriver.Chrome(options=u)

driver.get("https://demoqa.com/upload-download")
driver.maximize_window()

driver.find_element(By.XPATH,"//input[@id='uploadFile']").send_keys("C:\\Users\\Admin\Desktop\\mouse action.png")

driver.get("https://www.selenium.dev/downloads/")
driver.maximize_window()

driver.execute_script("window.scrollBy(0,1500)"," ")
time.sleep(2)
driver.find_element(By.XPATH,"//a[text()='4.12.1']").click()
