from selenium.webdriver.common.by import By
from locators.locators import Locators


class HomePage():

    def __init__(self, driver):
        self.driver = driver

        self.home = Locators.home_path
        self.logo = driver.find_element(By.CLASS_NAME, Locators.logo)
        self.courses = Locators.course_path
        self.blog = Locators.blog_path
        self.logout = Locators.logout

    def get_logo(self):
        return self.logo

    def click_courses(self):
        self.driver.find_element(By.XPATH, self.courses).click()
        self.driver.find_element(By.XPATH, self.home).click()

    def click_blog(self):
        self.driver.find_element(By.XPATH, self.blog).click()
        self.driver.find_element(By.XPATH, self.home).click()


