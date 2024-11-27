from pages.page_login import LoginPage
from pages.page_admin import AdminPage_DanhMuc
from pages.page_update import AdminPage_DanhMuc_Update
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


def generate_random_category_name(length=10):
    words = ['Blockchain', 'AI', 'Technology', 'Finance', 'Health', 'Education', 'Music', 'Science', 'Sports', 'Travel']
    random_word = random.choice(words)
    random_suffix = ''.join(random.choices(string.ascii_letters + string.digits, k=length))
    category_name = f"{random_word}_{random_suffix}"
    return category_name

class TestAdmin(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("http://localhost:3000/login") 
        self.driver.maximize_window()
        
    def go_to_danhmuc(self):
        loginPage = LoginPage(self.driver)
        loginPage.login()
        self.driver.get("http://localhost:3000/admin")
        menu_danhMuc_locator = (By.XPATH, '//button[@role="tab" and text()="Danh mục"]')
        menu_danhMuc = self.driver.find_element(*menu_danhMuc_locator)
        menu_danhMuc.click()
        time.sleep(2)
        
    def test_add_danhmuc_with_exist_name(self):
        self.go_to_danhmuc()
        danhmuc_page = AdminPage_DanhMuc(self.driver)
        danhmuc_page.set_new_danhmuc("Blockchain")
        danhmuc_page.click_add_danhmuc()
        time.sleep(1.5)
        message_locator = (By.XPATH, '//div[contains(text(),"Thêm danh mục thất bại: undefined")]')
        try:
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(message_locator)
            )
            assert True, "Thông báo xuất hiện: Thêm danh mục thất bại: undefined"
        except TimeoutException:
            assert False, "Thông báo không xuất hiện!"
    
       
    def test_add_danhmuc_with_not_exist_name(self):
        self.go_to_danhmuc()
        danhmuc_page = AdminPage_DanhMuc(self.driver)
        danhmuc_page.set_new_danhmuc(generate_random_category_name())
        danhmuc_page.click_add_danhmuc()
        time.sleep(0.5)
        message_locator = (By.XPATH, '//div[contains(text(),"Thêm danh mục thành công")]')
        try:
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(message_locator)
            )
            assert True, "Thông báo Thêm danh mục thành công xuất hiện"
        except TimeoutException:
            assert False, "Thông báo không xuất hiện!"
            
    def test_edit_danh_muc(self):
        self.go_to_danhmuc()
        danhmucPage = AdminPage_DanhMuc(self.driver)
        danhmucPage.click_random_edit_button()
        ##
        page_update = AdminPage_DanhMuc_Update(self.driver)
        current_name = page_update.get_curent_name()
        new_name = generate_random_category_name()
        page_update.set_new_name(new_name)
        ##
        page_update.click_cap_nhat()
        print(current_name)
        print("da clicked")
        print(new_name)
        time.sleep(2)
        message_locator = (By.XPATH, '//div[contains(text(),"Cập nhật danh mục thành công")]')
        try:
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(message_locator)
            )
            assert True, "Thông báo cập nhật danh mục thành công đã xuất hiện"
            self.driver.refresh()
            current_name_locator = (By.XPATH, f"//td[text()='{current_name}']")
            current_name_exists = len(self.driver.find_elements(*current_name_locator)) > 0
            assert not current_name_exists, f"Tên danh mục cũ '{current_name}' vẫn tồn tại trên trang"            
        except TimeoutException:
            assert False, "Thông báo không xuất hiện!"
            
    def test_delete_danh_muc(self):
        self.go_to_danhmuc()
        danhmucPage = AdminPage_DanhMuc(self.driver)
        danhmucPage.click_random_delete_button()
        time.sleep(1)
        xacnhan_locator = (By.XPATH, '//button[@type="button" and text()="Xác nhận"]')
        btn_xac_nhan = self.driver.find_element(*xacnhan_locator)
        btn_xac_nhan.click()
        time.sleep(2)
        message_locator = (By.XPATH, '//div[contains(text(),"Xóa danh mục thành công")]')
        try:
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(message_locator)
            )
            assert True, "Thông báo xóa danh mục thành công đã xuất hiện"       
        except TimeoutException:
            assert False, "Thông báo xóa thành công không xuất hiện!"


        
    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    runner = HtmlTestRunner.HTMLTestRunner(output="reports", report_name="test_admin_danhmuc", verbosity=2)
    unittest.main(testRunner=runner, exit=False)
