

class SS(object):

    def __init__(self, driver):
        self.driver = driver

    def screen_shot(self, path):
        directory = "/Users/dillanteagle/PycharmProjects/Selenium_webDriver_script/Screen_Shots"
        self.driver.get_screenshot_as_file(directory+path)