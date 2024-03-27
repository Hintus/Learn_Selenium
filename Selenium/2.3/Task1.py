import math
import os

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

from selenium.webdriver.support.select import Select

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/alert_accept.html")
    browser.find_element(By.TAG_NAME, 'button').click()
    browser.switch_to.alert.accept()
    browser.find_element(By.ID, 'answer').send_keys(
        math.log(abs(12 * math.sin(
            float(browser.find_element(By.ID, 'input_value').text)))))
    browser.find_element(By.TAG_NAME,'button').click()



finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()