
import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
import math
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
final = ''

@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome(executable_path=ChromeDriverManager().install())

    yield browser
    print("\nquit browser..")
    browser.quit()


class TestLogin:
    @pytest.mark.parametrize('URL', ["236895", "236896", "236897", "236898", "236899", "236903", "236904", "236905"])
    def test_guest_should_see_login_link(self, browser, URL):
        global final
        link = f"https://stepik.org/lesson//{URL}/step/1"
        browser.implicitly_wait(10)
        browser.get(link)
        a = str(math.log(int(time.time())))
        input1 = browser.find_element_by_tag_name('textarea')
        input1.send_keys(a)
        button = browser.find_element(By.CSS_SELECTOR, '.submit-submission')
        button.click()
        check_text = browser.find_element_by_css_selector('.smart-hints__hint').text
        try:
            assert 'Correct!' == check_text
        except AssertionError:
            final += check_text  # собираем ответ про Сов с каждой ошибкой
            print(final)


