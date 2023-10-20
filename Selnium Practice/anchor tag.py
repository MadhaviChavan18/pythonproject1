import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
a=Options()
a.add_experimental_option("detach",True)
driver=webdriver.Chrome(options=a)

driver.get("https://www.selenium.dev/documentation/webdriver/actions_api/wheel/")
time.sleep(2)
driver.find_element(By.LINK_TEXT,"Documentation").click()
time.sleep(2)

#multiple anchor tag find out by this code
anch=driver.find_elements(By.TAG_NAME,"a")
print(len(anch))
for abc in anch:
    print("Header Text:", abc.text)