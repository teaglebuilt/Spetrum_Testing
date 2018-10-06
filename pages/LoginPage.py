from locators.locators import Locators

class LoginPage():
    # Initialize state with Page Object Locators
    def __init__(self, driver):
        self.driver = driver

        self.username = Locators.username
        self.password = Locators.password
        self.login_btn = Locators.login_btn

    # test login username
    def enter_username(self, username):
        self.driver.find_element_by_id(self.username).clear()
        self.driver.find_element_by_id(self.username).send_keys(username)

    # test login password
    def enter_password(self, password):
        self.driver.find_element_by_id(self.password).clear()
        self.driver.find_element_by_id(self.password).send_keys(password)

    # submit login form
    def click_login(self):
        self.driver.find_element_by_tag_name(self.login_btn).click()