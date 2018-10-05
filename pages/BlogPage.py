from locators.locators import Locators
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

class BlogPage():

    def __init__(self, driver):
        self.driver = driver

        self.search_posts = Locators.post_search
        self.post = Locators.post
        self.post_tag = Locators.post_tag

    def search_posts(self, search_term):
        search_box = self.driver.find_element(By.NAME, "q")
        search_box.send_keys(search_term, Keys.RETURN)
        posts = self.driver.find_element_by_class_name(self.post)
        results = []
        for post in posts:
            title = post.get_attribute("title")
            print(title)
            results.append(title)
