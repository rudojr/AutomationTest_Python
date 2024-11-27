from selenium.webdriver.common.by import By
import random
import time

class UploadArticle:
    def __init__(self, driver):
        self.driver = driver
        self.file_input_locator = (By.XPATH, '//input[@accept="image/*" and @id="raised-button-file"]')
        self.title = (By.ID, 'title')
        self.category = (By.ID, 'category')
        self.content = (By.XPATH, '//div[@contenteditable="true" and @role="textbox"]')
        self.btn_dang_bai = (By.XPATH, '//button[@type="submit"]')
    
    def upload_image(self, img_path):
        file_input = self.driver.find_element(*self.file_input_locator)
        file_input.send_keys(img_path)    
    
    def set_title(self, title):
        txt_title = self.driver.find_element(*self.title)
        txt_title.send_keys(title)
    
    def select_random_category(self):
        category_dropdown = self.driver.find_element(*self.category)
        category_dropdown.click()
        time.sleep(0.5)
        options = self.driver.find_elements(By.XPATH, './/li[@role="option"]')
        random_option = random.choice(options)
        random_option.click()
    
    def set_content(self, content):
        txt_content = self.driver.find_element(*self.content)
        txt_content.click()
        txt_content.send_keys(content)
        
    def click_dang_bai(self):
        btn_dangbai = self.driver.find_element(*self.btn_dang_bai)
        btn_dangbai.click()
        time.sleep(0.5)