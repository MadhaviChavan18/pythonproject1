import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
a=Options()
a.add_experimental_option("detach",True)
driver=webdriver.Chrome(options=a)

driver.get("https://demo.automationtesting.in/Windows.html")
driver.maximize_window()
driver.find_element(By.XPATH,"//a[@href='http://www.selenium.dev']//button[@class='btn btn-info'][normalize-space()='click']").click()

print(driver.current_window_handle) #parent window value
handel=driver.window_handles
#more than one window handle
for h in handel:
    driver.switch_to.window(h)
    print(driver.title)
#for close particular window

if driver.title=="Frames & windows":
    driver.close()

'''driver.get("https://demoqa.com/browser-windows")
driver.maximize_window()
driver.find_element(By.XPATH,"//div[@class='element-group'][3]").click()
driver.find_element(By.ID,"tabButton").click()
print(driver.current_window_handle)
handel1=driver.window_handles# handel is variable
for nt in handel1:
    driver.switch_to.window(nt)
    print(driver.title)
time.sleep(2)
driver.close()'''


driver.get("https://demoqa.com/browser-windows")
driver.find_element(By.XPATH,"//button[@id='windowButton']").click()
print(driver.current_window_handle)
handel2=driver.window_handles
for nw in handel2:
    print(driver.switch_to.window(nw))
    print(driver.title)

print("On DemoQa site")
time.sleep(2)
driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()
driver.find_element(By.XPATH,"//button[@onclick='myFunction()']").click()
time.sleep(2)
print(driver.current_window_handle)
handel4=driver.window_handles
for nbw in handel4:
    print(driver.switch_to.window(nbw))
print("On testautomationpractice.blogspot site")
