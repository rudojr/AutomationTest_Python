from selenium.webdriver.common.by import By
import random

class AdminPage_DanhMuc:
    def __init__(self, driver):
        self.driver = driver
        self.txt_danhMuc = (By.XPATH, '//input[@type="text"]')
        self.btn_addDanhMuc = (By.XPATH, '//button[@type="button" and text()="Thêm danh mục"]')
        self.btn_Edit = (By.XPATH, '//button[@type="button" and text()="Sửa"]')
        self.btn_delete = (By.XPATH, '//button[@type="button" and text()="Xóa"]')   
   
         
    def set_new_danhmuc(self, danhMucName):
        txtDanhMuc = self.driver.find_element(*self.txt_danhMuc)
        txtDanhMuc.clear()
        txtDanhMuc.send_keys(danhMucName)
    
    def click_add_danhmuc(self):
        btnAddDanhMuc = self.driver.find_element(*self.btn_addDanhMuc)
        btnAddDanhMuc.click()
        
    def click_random_edit_button(self):
        edit_buttons = self.driver.find_elements(*self.btn_Edit)
        if len(edit_buttons)==0:
            return
        random_list  = edit_buttons[6:]
        random_edit_button = random.choice(random_list)
        random_edit_button.click()
        
    def click_random_delete_button(self):
        delete_buttons = self.driver.find_elements(*self.btn_delete)
        if len(delete_buttons)==0:
            return
        delete_button = delete_buttons[-1]
        delete_button.click()