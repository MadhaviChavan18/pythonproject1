import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium .webdriver.common.by import By
a=Options()
a.add_experimental_option("detach",True)
driver=webdriver.Chrome(options=a)
#orange HRM site
driver.get("https://opensource-demo.orangehrmlive.com/")
print(driver.title)
driver.maximize_window()
time.sleep(2)
driver.find_element(By.NAME,"username").send_keys("Admin")
time.sleep(2)
driver.find_element(By.NAME,"password").send_keys("admin123")
driver.find_element(By.XPATH,"//button[@type='submit']").click()
#demoQa site
driver.get("https://demoqa.com/")
time.sleep(2)
print(driver.title)
driver.maximize_window()
driver.find_element(By.XPATH,"//div[@class='category-cards']//div[@class='card mt-4 top-card'][1]").click()
time.sleep(2)
#backto the orange HRM
driver.back()
time.sleep(2)
driver.back()
time.sleep(2)
driver.forward()
time.sleep(2)
driver.forward()
driver.find_element(By.XPATH,"//div[@class='element-list collapse show']//li[@id='item-0']").click()
driver.find_element(By.ID,"userName").send_keys("Madhavi Chavan")
time.sleep(2)
driver.find_element(By.ID,"userEmail").send_keys("abc@gmail.com")
time.sleep(2)
driver.find_element(By.ID,"currentAddress").send_keys("Keshavnagar,pune")
time.sleep(2)
driver.find_element(By.ID,"permanentAddress").send_keys("Pune")
time.sleep(2)
#driver.find_element(By.ID,"submit").click()