import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

a=Options()
a.add_experimental_option("detach",True)
driver=webdriver.Chrome(options=a)

driver.get("https://demoqa.com/")
driver.maximize_window()
driver.find_element(By.XPATH,"//div[@class='category-cards']//div[@class='card mt-4 top-card'][1]").click()
driver.find_element(By.XPATH,"//span[text()='Radio Button']").click()
time.sleep(2)
rediob=driver.find_element(By.XPATH,"//label[@for='yesRadio']")
if rediob.is_selected():
    pass
else:
    rediob.click()
driver.get("https://artoftesting.com/samplesiteforselenium")
driver.find_element(By.XPATH,"//input[@type='radio'][1]").click()
print("Radio button clicked")
driver.close()

