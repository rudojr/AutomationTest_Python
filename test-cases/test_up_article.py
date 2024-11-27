from pages.page_login import LoginPage
from pages.page_up_news import UploadArticle
from pages.page_home import HomePage
import unittest
import time
import random
import string
from selenium.common.exceptions import TimeoutException
import HtmlTestRunner
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

def generate_random_title(max_length=50):
    title_length = random.randint(1, max_length)
    title = ''.join(random.choices(string.ascii_letters + string.digits + " ", k=title_length))
    return title
    
class TestNewArticle(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("http://localhost:3000/login") 
        self.driver.maximize_window()
        self.random_title = generate_random_title()

        
    def go_to_write(self):
        loginPage = LoginPage(self.driver)
        loginPage.login()
        new_article_locator = (By.XPATH,'//a[text()="Viết bài"]')
        btn_viet_bai = self.driver.find_element(*new_article_locator)
        btn_viet_bai.click()
        time.sleep(2)
    
    def test_noti_when_save_with_null_data(self):
        self.go_to_write()
        upload_page = UploadArticle(self.driver)
        upload_page.click_dang_bai()
        message_locator = (By.XPATH, '//div[contains(text(), "Tất cả các trường phải được điền")]') 
        try:
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(message_locator)
            )
            print("Thông báo đã xuất hiện.")
        except TimeoutException:
            print("Thông báo không xuất hiện trong 10 giây.")
    
    def test_load_image(self):
        self.go_to_write()
        upload_page = UploadArticle(self.driver)
        upload_page.upload_image(r"D:\\Python\\Automation\\scripts-test\\images\\block_chain.jpg")
        image_locator = (By.XPATH, '//img[@alt="Ảnh bìa"]')
        try:
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(image_locator)
            )
            print("Ảnh bìa đã được tải lên và hiển thị thành công.")
        except TimeoutException:
            print("Ảnh bìa không hiển thị sau khi tải lên. Kiểm tra lại.")

    
    def test_up_article(self):
        self.go_to_write()
        upload_page = UploadArticle(self.driver)
        upload_page.upload_image(r"D:\\Python\\Automation\\scripts-test\\images\\block_chain.jpg")
        upload_page.set_title(self.random_title)
        upload_page.select_random_category()
        upload_page.set_content("Đây là nội dung bài báo về block chain")
        upload_page.click_dang_bai()
        message_locator = (By.XPATH, '//div[contains(text(), "Bài viết đã được đăng thành công")]') 
        try:
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(message_locator)
            )
            print("Thông báo đã xuất hiện.")
        except TimeoutException:
            print("Thông báo không xuất hiện trong 10 giây.")

    def test_verify_article_after_up(self):
        loginPage = LoginPage(self.driver)
        loginPage.login()
        homePage = HomePage(self.driver)
        homePage.input_search(self.random_title)

    
    def tearDown(self):
        self.driver.quit()
        
if __name__ == "__main__":
    runner = HtmlTestRunner.HTMLTestRunner(output="reports", report_name="test_login_report", verbosity=2)
    unittest.main(testRunner=runner, exit=False)