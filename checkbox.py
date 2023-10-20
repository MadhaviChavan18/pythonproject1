import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

option=Options()
option.add_experimental_option("detach",True)
driver=webdriver.Chrome(options=option)

driver.get("https://demoqa.com/")
driver.maximize_window()
driver.find_element(By.XPATH,"//div[@class='category-cards']//div[@class='card mt-4 top-card'][1]").click()
time.sleep(2)
driver.find_element(By.XPATH,"//div[@class='element-list collapse show']//li[@id='item-1']").click()
time.sleep(2)

checkbox=driver.find_element(By.XPATH,"//span[@class='rct-checkbox']")
if checkbox.is_selected():
    pass
else:
    checkbox.click()
    print("click action perform")
driver.close()