import math
import os

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

from selenium.webdriver.support.select import Select

try:
    browser = webdriver.Chrome()
    browser.get("https://suninjuly.github.io/file_input.html")
    browser.find_element(By.NAME, "firstname").send_keys('Егор')
    browser.find_element(By.NAME, "lastname").send_keys('Хина')
    browser.find_element(By.NAME, "email").send_keys('egorhina@inbox.ru')
    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, 'nothing.txt')
    browser.find_element(By.ID, "file").send_keys(file_path)
    browser.find_element(By.TAG_NAME, 'button').click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()
