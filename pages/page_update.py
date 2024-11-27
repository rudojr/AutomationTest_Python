from selenium.webdriver.common.by import By


class AdminPage_DanhMuc_Update:
    def __init__(self, driver):
        self.driver = driver
        self.txt_input = (By.XPATH, '//input[@type="text"]')
        self.btn_update = (By.XPATH, '//button[@type="button" and text()="Cập nhật"]')
    
    def get_curent_name(self):
        return self.driver.find_elements(*self.txt_input)[1].get_attribute('value')

    
    def set_new_name(self,name):
        txt_current_name = self.driver.find_elements(*self.txt_input)[1]
        txt_current_name.clear()
        txt_current_name.send_keys(name)
    
    def click_cap_nhat(self):
        btn_cap_nhat = self.driver.find_element(*self.btn_update)
        btn_cap_nhat.click()
