from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))
browser = webdriver.Chrome(executable_path=ChromeDriverManager().install())

# говорим WebDriver искать каждый элемент в течение 5 секунд
browser.implicitly_wait(5)
browser.get("http://suninjuly.github.io/explicit_wait2.html")
button = browser.find_element(By.CSS_SELECTOR, '.btn.btn-primary')
# говорим Selenium проверять в течение 5 секунд, пока кнопка не станет кликабельной
price = WebDriverWait(browser, 15).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "100")
    )

button.click()

x_element = browser.find_element_by_id("input_value")
x = x_element.text
y = calc(x)
print(y)
input1 = browser.find_element(By.CSS_SELECTOR, '.form-control')
input1.send_keys(y)
button_2 = browser.find_element_by_id('solve')
browser.execute_script("return arguments[0].scrollIntoView(true);", button_2)
button_2.click()
browser.quit()



