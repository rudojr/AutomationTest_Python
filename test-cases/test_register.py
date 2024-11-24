import unittest
import time
import random
import string
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from pages.page_register import RegisterPage

def generate_random_email():
    domain="gmail.com"
    length = random.randint(8, 25)
    username = ''.join(random.choices(string.ascii_lowercase + string.digits, k=length))
    email = f"{username}@{domain}"
    return email

class TestRegister(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("http://localhost:3000/register") 
        self.driver.maximize_window()

    def test_missing_required_fields(self):
        register_page = RegisterPage(self.driver)
        register_page.set_name("")
        register_page.set_email("")
        register_page.set_password("")
        register_page.set_confirm_password("")
        register_page.click_button_register()
        time.sleep(0.5)
        error_message = self.driver.find_element(By.CSS_SELECTOR, '[role="alert"]')
        self.assertTrue(error_message.is_displayed(), "Error message is not displayed on the page")
        self.assertEqual(error_message.text, "Please add all fields")
        
    def test_invalid_email(self):
        register_page = RegisterPage(self.driver)
        register_page.set_name("John Doe")
        register_page.set_email("invalid-email")
        register_page.set_password("Secure@123")
        register_page.set_confirm_password("Secure@123")
        register_page.click_button_register()
        time.sleep(0.5)
        error_message = self.driver.find_element(By.CSS_SELECTOR, '[role="alert"]')
        self.assertTrue(error_message.is_displayed(), "Error message is not displayed on the page")
        self.assertEqual(error_message.text, "Email must be a valid email address")
    
    def test_password_mismatch(self):
        register_page = RegisterPage(self.driver)
        register_page.set_name("John Doe")
        register_page.set_email("johndoe@example.com")
        register_page.set_password("Secure@123")
        register_page.set_confirm_password("Different@123")
        register_page.click_button_register()
        time.sleep(0.5)
        error_message = self.driver.find_element(By.CSS_SELECTOR, '[role="alert"]')
        self.assertTrue(error_message.is_displayed(), "Error message is not displayed on the page")
        self.assertEqual(error_message.text, "Mật khẩu không khớp")

    def test_weak_password(self):
        register_page = RegisterPage(self.driver)
        register_page.set_name("John Doe")
        register_page.set_email("johndoe@example.com")
        register_page.set_password("123")
        register_page.set_confirm_password("123")
        register_page.click_button_register()
        time.sleep(0.5)
        error_message = self.driver.find_element(By.CSS_SELECTOR, '[role="alert"]')
        self.assertTrue(error_message.is_displayed(), "Error message is not displayed on the page")
        self.assertEqual(error_message.text, "Password must be length of greater than 6")
    
    def test_valid_registration(self):
        register_page = RegisterPage(self.driver)
        register_page.set_name("John Doe")
        register_page.set_email(generate_random_email())
        register_page.set_password("Secure@123")
        register_page.set_confirm_password("Secure@123")
        register_page.click_button_register()
        time.sleep(1)
        user_account_button = self.driver.find_element(By.XPATH, '//button[@aria-label="account of current user"]')
        self.assertTrue(user_account_button.is_displayed(), "User account button is not displayed, login might have failed.")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()