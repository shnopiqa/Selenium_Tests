from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

link = "http://selenium1py.pythonanywhere.com/"


class TestMainPage1():

    @classmethod
    def setup_class(self):
        print("\nstart browser for test suite..")
        self.browser = webdriver.Chrome(executable_path=ChromeDriverManager().install())

    @classmethod
    def teardown_class(self):
        print("quit browser for test suite..")
        self.browser.quit()

    def test_guest_should_see_login_link(self):
        print('start test link 1')
        self.browser.get(link)
        self.browser.find_element_by_css_selector("#login_link")

    def test_guest_should_see_basket_link_on_the_main_page(self):
        print('start test basket 1')
        self.browser.get(link)
        self.browser.find_element_by_css_selector(".basket-mini .btn-group > a")


class TestMainPage2():

    def setup_method(self):
        print("start browser for test..")
        self.browser = webdriver.Chrome(executable_path=ChromeDriverManager().install())

    def teardown_method(self):
        print("quit browser for test..")
        self.browser.quit()

    def test_guest_should_see_login_link(self):
        print('start test link 2')
        self.browser.get(link)
        self.browser.find_element_by_css_selector("#login_link")

    def test_guest_should_see_basket_link_on_the_main_page(self):
        print('start test basket 2')
        self.browser.get(link)
        self.browser.find_element_by_css_selector(".basket-mini .btn-group > a")

