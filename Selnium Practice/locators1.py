import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

a=Options()
a.add_experimental_option("detach",True)
driver=webdriver.Chrome(options=a)

driver.get("https://opensource-demo.orangehrmlive.com/")
print(driver.title)
driver.maximize_window()
time.sleep(2)
driver.find_element(By.NAME,"username").send_keys("Admin")
time.sleep(2)
driver.find_element(By.NAME,"password").send_keys("admin123")
driver.find_element(By.XPATH,"//button[@type='submit']").click()
time.sleep(4)
print("successfully log in Orange HRM")

driver.get("https://www.facebook.com/")
print(driver.title)
driver.maximize_window()
time.sleep(2)
driver.find_element(By.NAME,"email").send_keys("madhu18061991@gmail.com")
time.sleep(2)
driver.find_element(By.ID,"pass").send_keys("madhu@169")
time.sleep(2)
driver.find_element(By.NAME,"login").click()
print("successfully login in facebook")
driver.close()

