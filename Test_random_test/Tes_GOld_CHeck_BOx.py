from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
import time
import math
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

def check_box_test():
    try:
        link = 'http://suninjuly.github.io/get_attribute.html'
        browser = webdriver.Chrome(executable_path=ChromeDriverManager().install())
        browser.get(link)
        x_element = browser.find_element_by_id("treasure")
        x = x_element.get_attribute("valuex")
        print(x)

        y = calc(x)
        print(y)
        input1 = browser.find_element_by_id('answer')
        input1.send_keys(y)
        option1 = browser.find_element_by_id("robotsRule")
        option1.click()
        option2 = browser.find_element_by_id("robotCheckbox")
        option2.click()
        button = browser.find_element_by_css_selector(".btn.btn-default")
        button.click()
    finally:
        # успеваем скопировать код за 30 секунд
        time.sleep(30)
                    # закрываем браузер после всех манипуляций
    browser.quit()
check_box_test()