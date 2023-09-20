from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.get("https://www.tyehdbt.com/checkouts/458f8bc75f3e5a4d209a6b9c292ec407?step=contact_information")

country_field = driver.find_element(By.ID, "country")
country = Select(country_field)
country.select_by_visible_text("United States")

state_field = driver.find_element(By.ID, "administrative_area_level_1")
state = Select(state_field)
state.select_by_visible_text("California")

zip_code_field = driver.find_element(By.ID, "postal_code")
zip_code_field.send_keys("30006")

sleep(1)
phone_field = driver.find_elements(By.NAME, "phone")
phone_field[1].send_keys("17771441009")
driver.quit()
