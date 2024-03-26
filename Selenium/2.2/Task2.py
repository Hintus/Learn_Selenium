import math

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

from selenium.webdriver.support.select import Select

try:
    browser = webdriver.Chrome()
    browser.get("https://suninjuly.github.io/execute_script.html")
    browser.find_element(By.ID, 'answer').send_keys(
        math.log(abs(12 * math.sin(
            float(browser.find_element(By.ID, 'input_value').text)))))
    check = browser.find_element(By.ID, 'robotCheckbox')
    browser.execute_script("return arguments[0].scrollIntoView(true);", check)
    check.click()
    browser.find_element(By.ID, 'robotsRule').click()
    browser.find_element(By.TAG_NAME, 'button').click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()
