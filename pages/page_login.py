from selenium.webdriver.common.by import By

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.txtEmail = (By.XPATH, '//input[@id="email"]')
        self.txtPassword = (By.XPATH, '//input[@id="password"]')
        self.btnDangNhap = (By.XPATH, '//button[@type="submit"]')
        
    def set_email(self, email):
        email_field = self.driver.find_element(*self.txtEmail)
        email_field.clear()
        email_field.send_keys(email)

    def set_password(self, password):
        password_field = self.driver.find_element(*self.txtPassword)
        password_field.clear()
        password_field.send_keys(password)
    
    def click_button_login(self):
        btnDangKy = self.driver.find_element(*self.btnDangNhap)
        btnDangKy.click()
        