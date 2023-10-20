import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

a=Options()
a.add_experimental_option("detach",True)
driver=webdriver.Chrome(options=a)

driver.get("http://omayo.blogspot.com/")
driver.maximize_window()

drop1=Select(driver.find_element(By.ID,'drop1'))
# By visible text method
time.sleep(2)
drop1.select_by_visible_text("doc 2")

#by value method
time.sleep(2)
drop1.select_by_value("mno")
#by index method
time.sleep(2)
drop1.select_by_index(0)
#count no of options
print(len(drop1.options))
#capture options from dropdown
all1=drop1.options
for drp1 in all1:
    print(drp1.text)

driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()
print(driver.title)

drop2=Select(driver.find_element(By.ID,'dropdown-class-example'))
time.sleep(2)
drop2.select_by_visible_text("Select")
drop2.select_by_value("option2")
drop2.select_by_index(2)
print(len(drop2.options))
all2=drop2.options
for drp2 in all2:
    print(drp2.text)

driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()
driver.execute_script("window.scrollBy(0,550)"," ")
drop3=Select(driver.find_element(By.XPATH,"//div[@class='form-group']//select[@id='country']"))
time.sleep(2)
drop3.select_by_visible_text("Canada")
time.sleep(2)
drop3.select_by_value("china")
drop3.select_by_index(6)
print(len(drop3.options))
all3=drop3.options
for drp3 in all3:
    print(drp3.text)



