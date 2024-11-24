import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import HtmlTestRunner
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from pages.page_login import LoginPage

class TestLogin(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("http://localhost:3000/login") 
        self.driver.maximize_window()
    
    def test_missing_required_fields(self):
        login_page = LoginPage(self.driver)
        login_page.set_email("")
        login_page.set_password("")
        login_page.click_button_login()
        time.sleep(0.5)
        error_message = self.driver.find_element(By.CSS_SELECTOR, '[role="alert"]')
        self.assertTrue(error_message.is_displayed(), "Error message is not displayed on the page")
        self.assertEqual(error_message.text, "Không tồn tại người dùng này")
        
    def test_missing_password_fields(self):
        login_page = LoginPage(self.driver)
        login_page.set_email("admin@gmail.com")
        login_page.set_password("")
        login_page.click_button_login()
        time.sleep(0.5)
        error_message = self.driver.find_element(By.CSS_SELECTOR, '[role="alert"]')
        self.assertTrue(error_message.is_displayed(), "Error message is not displayed on the page")
        self.assertEqual(error_message.text, "Sai mật khẩu")
    
    def test_login_incorrect_password(self):
        login_page = LoginPage(self.driver)
        login_page.set_email("admin@gmail.com")
        login_page.set_password("admin1234")
        login_page.click_button_login()
        time.sleep(0.5)
        error_message = self.driver.find_element(By.CSS_SELECTOR, '[role="alert"]')
        self.assertTrue(error_message.is_displayed(), "Error message is not displayed on the page")
        self.assertEqual(error_message.text, "Sai mật khẩu")
    
    def test_login_successfully(self):
        login_page = LoginPage(self.driver)
        login_page.set_email("admin@gmail.com")
        login_page.set_password("admin123")
        login_page.click_button_login()
        time.sleep(0.5)
        user_account_button = self.driver.find_element(By.XPATH, '//button[@aria-label="account of current user"]')
        self.assertTrue(user_account_button.is_displayed(), "User account button is not displayed, login might have failed.")
    
    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    runner = HtmlTestRunner.HTMLTestRunner(output="reports", report_name="test_login_report", verbosity=2)
    unittest.main(testRunner=runner, exit=False)