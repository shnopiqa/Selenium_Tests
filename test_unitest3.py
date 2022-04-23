from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math
import unittest


def get_url(url: str) -> str:
    """Функция выполняет регистацию на сайте
       и возвращает текст 'Congratulations! You have successfully registered!'
       при успешной регистрации.
    """
    browser = webdriver.Chrome(executable_path=ChromeDriverManager().install())
    browser.get(url)
    browser.find_element(By.CSS_SELECTOR, ".first_block input.first").send_keys("Имя")
    browser.find_element(By.CSS_SELECTOR, ".first_block input.second").send_keys("Фамилия")
    browser.find_element(By.CSS_SELECTOR, ".first_block input.third").send_keys("Email")
    browser.find_element(By.XPATH, "//button['Submit']").click()
    text_reg = browser.find_element(By.TAG_NAME, "h1").text
    browser.quit()
    return text_reg


class TestRegistration(unittest.TestCase):
    def test_registration1(self):
        text = get_url('http://suninjuly.github.io/registration1.html')
        self.assertEqual("Congratulations! You have successfully registered!", text)

    def test_registration2(self):
        text = get_url('http://suninjuly.github.io/registration2.html')
        self.assertEqual("Congratulations! You have successfully registered!", text)


if __name__ == "__main__":
    unittest.main()
