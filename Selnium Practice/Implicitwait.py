from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
w=Options()
w.add_experimental_option("detach",True)
driver=webdriver.Chrome(options=w)

driver.get("https://demo.guru99.com/test/newtours/")
driver.maximize_window()

driver.implicitly_wait(50)
driver.find_element(By.NAME,"userName").send_keys("ABC")
driver.find_element(By.XPATH,"//input[@name='password']").send_keys("abc@123")
driver.find_element(By.NAME,"submit").click()

driver.get("https://chercher.tech/practice/implicit-wait-example")
driver.maximize_window()
driver.implicitly_wait(50)
driver.find_element(By.XPATH,'//*[@id="q"]/input[1]').click()

driver.find_element(By.XPATH,'//*[@id="q"]/input[5]').click()