from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
import time
import math
from selenium.webdriver.support.ui import Select
def calc(x,y):
  return str(str(int(x)+int(y)))

def check_box_test():
    try:
        link = 'http://suninjuly.github.io/selects2.html'
        browser = webdriver.Chrome(executable_path=ChromeDriverManager().install())
        browser.get(link)
        x_element = browser.find_element_by_id("num1")
        x = x_element.text
        y_element = browser.find_element_by_id("num2")
        y = y_element.text
        sum_1 = calc(x,y)
        print(sum_1)
        select = Select(browser.find_element_by_tag_name("select"))
        select.select_by_value(sum_1)
        button = browser.find_element_by_css_selector(".btn.btn-default")
        button.click()
    finally:
        # успеваем скопировать код за 30 секунд
        time.sleep(30)
                    # закрываем браузер после всех манипуляций
    browser.quit()
check_box_test()