import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
m=Options()
m.add_experimental_option("detach",True)
driver=webdriver.Chrome(options=m)
 #double click
driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()
driver.find_element(By.XPATH,"//input[@id='field1']").send_keys("Hello Python")
act=ActionChains(driver)#importand line for mouse action
driver.execute_script("window.scrollBy(0,500)","")
time.sleep(2)
double_click=driver.find_element(By.XPATH,"//button[@ondblclick='myFunction1()']")
act.double_click(double_click).perform()
print("Hello world Hello python")

contextclick=driver.find_element(By.XPATH,"//button[@onclick='myFunctionAlert()']")
act.context_click(contextclick).perform()

#drag drop
source=driver.find_element(By.XPATH,"//p[normalize-space()='Drag me to my target']")
target=driver.find_element(By.XPATH,"//div[@id='droppable']")
act.drag_and_drop(source,target).perform()

