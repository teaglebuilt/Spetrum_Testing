import unittest
from selenium import webdriver
import datetime
from pages.LoginPage import LoginPage
from pages.HomePage import HomePage
from test_utility.screen_shot import SS
import HtmlTestRunner

# test case for login
# connected Page Objects - LoginPage, HomePage

class Test_Login(unittest.TestCase):

    # Set up Test Case
    @classmethod
    def setUp(cls):
        cls.driver = webdriver.Chrome(executable_path="/usr/local/bin/chromedriver")
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()
        print("Test Run started at :" + str(datetime.datetime.now()))
        print("Chrome Environment Set Up")
        print("================================================")


    # Execute Test Case
    def test_01_login_valid(self):
        # Initiate Driver
        driver = self.driver
        driver.get("http://104.248.66.202/memberships/login/")
        # Pass in Driver for ScreenShot
        ss = SS(driver)
        ss_path = "/"
        # Pass in Driver to LoginPage
        login = LoginPage(driver)
        login.enter_username("administrator")
        login.enter_password("Dexter4212")
        login.click_login()
        # Pass in driver to Homepage
        homepage = HomePage(driver)
        homepage.get_logo()
        homepage.click_courses()
        homepage.click_blog()
        # Take screen shot
        ss.screen_shot(ss_path+"home.png")

    # Tear down test case
    @classmethod
    def tearDown(cls):
        if cls.driver is not None:
            print("================================================")
            cls.driver.close()
            cls.driver.quit()
            print("Test Complete")


# Also generates report
if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output="/Users/dillanteagle/PycharmProjects/Selenium_webDriver_script/reports"))




