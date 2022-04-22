from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import os
import time
try:
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome(executable_path=ChromeDriverManager().install())
    browser.get(link)
    input1 = browser.find_element(By.CSS_SELECTOR, "[name='firstname']")
    input1.send_keys('Владимир')
    input2 = browser.find_element(By.CSS_SELECTOR, "[name='lastname']")
    input2.send_keys('Иванович')
    input3 = browser.find_element(By.CSS_SELECTOR, "[name='email']")
    input3.send_keys('ЗУбенко')
    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_name = "File.txt"
    file_path = os.path.join(current_dir, file_name)
    element = browser.find_element(By.CSS_SELECTOR, "[type='file']")
    element.send_keys(file_path)
    button = browser.find_element_by_css_selector(".btn.btn-primary")
    button.click()
finally:
    time.sleep(30)
    # закрываем браузер после всех манипуляций
browser.quit()

