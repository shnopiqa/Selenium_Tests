from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math
import unittest

class TestAnk(unittest.TestCase):
    def test1(self):
        link1 = "http://suninjuly.github.io/registration1.html"
        browser = webdriver.Chrome(executable_path=ChromeDriverManager().install())
        browser.get(link1)
        element_first = browser.find_element(By.XPATH, "/html/body/div/form/div[1]/div[1]/input")
        element_first.send_keys("Пиво")
        element_second = browser.find_element(By.XPATH, "/html/body/div/form/div[1]/div[2]/input")
        element_second.send_keys("Пиво")
        element_mail = browser.find_element(By.XPATH, "/html/body/div/form/div[1]/div[3]/input")
        element_mail.send_keys("Пиво")
        button = browser.find_element(By.CSS_SELECTOR, "body > div > form > button")
        button.click()
        time.sleep(1)
        welcome_text_elt = browser.find_element(By.CSS_SELECTOR, "body > div > h1")
        welcome_text = welcome_text_elt.text
        self.assertEquals(welcome_text, "Congratulations! You have successfully registered!",
                          "Should be successfully registered")

    def test2(self):
        link2 = "http://suninjuly.github.io/registration2.html"
        browser = webdriver.Chrome(executable_path=ChromeDriverManager().install())
        browser.get(link2)
        element_first = browser.find_element(By.XPATH, "/html/body/div/form/div[1]/div[1]/input")
        element_first.send_keys("Пиво")
        element_second = browser.find_element(By.XPATH, "/html/body/div/form/div[1]/div[2]/input")
        element_second.send_keys("Пиво")
        element_mail = browser.find_element(By.XPATH, "/html/body/div/form/div[1]/div[3]/input")
        element_mail.send_keys("Пиво")
        button = browser.find_element(By.CSS_SELECTOR, "body > div > form > button")
        button.click()
        time.sleep(1)
        welcome_text_elt = browser.find_element(By.CSS_SELECTOR, "body > div > h1")
        welcome_text = welcome_text_elt.text
        self.assertEquals(welcome_text, "Congratulations! You have successfully registered!",
                          "Should be successfully registered")


if __name__ == "__main__":
    unittest.main()