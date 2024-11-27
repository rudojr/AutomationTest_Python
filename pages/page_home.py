from selenium.webdriver.common.by import By

class HomePage:
    def __init__(self, driver):
        self.driver = driver
        self.txt_input_search = (By.XPATH, '//input[@type="text"]')
    
    def input_search(self, keyword):
        txt_search = self.driver.find_element(*self.txt_input_search)
        txt_search.clear()
        txt_search.send_keys(keyword)