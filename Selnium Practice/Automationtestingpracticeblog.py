from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver import ActionChains

atp=Options()
atp.add_experimental_option("detach",True)
driver=webdriver.Chrome(options=atp)

driver.get("https://testautomationpractice.blogspot.com/")
driver.find_element(By.XPATH,"//input[@class='form-control'][1]").send_keys("Madhavi Chavan")
driver.find_element(By.XPATH,"//input[@class='form-control'][2]").send_keys("madhu180619991@gmail.com")
driver.close()
