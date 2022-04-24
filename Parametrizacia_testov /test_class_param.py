import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


@pytest.mark.parametrize('language', ["ru", "en-gb"])
class TestLogin:
    browser = webdriver.Chrome(executable_path=ChromeDriverManager().install())
    def test_guest_should_see_login_link(self, browser, language):
        link = f"http://selenium1py.pythonanywhere.com/{language}/"
        browser.get(link)
        browser.find_element_by_css_selector("#login_link")
        # этот тест запустится 2 раза

    def test_guest_should_see_navbar_element(self, browser, language):
       pass