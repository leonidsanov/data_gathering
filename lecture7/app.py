from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()
driver.get("https://www.amazon.com")

search_box = driver.find_element(By.ID, 'twotabsearchtextbox')
search_box.send_keys("laptops")
search_box.submit()

assert "laptops" in driver.title