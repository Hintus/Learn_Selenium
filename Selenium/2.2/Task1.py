from selenium import webdriver
from selenium.webdriver.common.by import By
import time

from selenium.webdriver.support.select import Select

try:
    browser = webdriver.Chrome()
    browser.get("https://suninjuly.github.io/selects1.html")
    x = int(browser.find_element(By.ID, 'num1').text) + int(browser.find_element(By.ID, 'num2').text)
    Select(browser.find_element(By.TAG_NAME, "select")).select_by_value(f'{x}')
    browser.find_element(By.TAG_NAME, "button").click()
finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()
