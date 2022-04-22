from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))
link = 'http://suninjuly.github.io/redirect_accept.html'
browser = webdriver.Chrome(executable_path=ChromeDriverManager().install())
browser.get(link)
button = browser.find_element(By.CSS_SELECTOR, '.trollface.btn.btn-primary')
button.click()
new_window = browser.window_handles[1]
browser.switch_to.window(new_window)
x_element = browser.find_element(By.ID, 'input_value')
x = x_element.text
print(x)
y = calc(x)
input1 = browser.find_element(By.CSS_SELECTOR, '.form-control')
input1.send_keys(y)
button_2 = browser.find_element(By.CSS_SELECTOR, '.btn.btn-primary')
button_2.click()
