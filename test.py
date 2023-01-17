import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome('/venv/bin/chromedriver')  # Optional argument, if not specified will search path.

driver.get('https://rahulshettyacademy.com/angularpractice/')

name = driver.find_element(By.NAME, "name")
name.send_keys("Lukas")

email = driver.find_element(By.NAME, "email")
email.send_keys("email@domain.com")

password = driver.find_element(By.ID, "exampleInputPassword1")
password.send_keys("password12")

checkbox = driver.find_element(By.ID, "exampleCheck1")
checkbox.click()

gender = driver.find_element(By.ID, "exampleFormControlSelect1")
Select(gender).select_by_visible_text("Female")

employment = driver.find_element(By.ID, "inlineRadio2")
employment.click()

date = driver.find_element(By.NAME, "bday")
date.send_keys("1983-11-06")

submit = driver.find_element(By.CLASS_NAME, "btn-success")
submit.click()

success = driver.find_element(By.CSS_SELECTOR, "div.alert > :nth-child(1)").text
if success.__contains__("Success!"): print("Success message was displayed!")
else: print("Success message was NOT displayed!")

time.sleep(1)