from selenium.webdriver.common.by import By

class RegisterPage:
    def __init__(self, driver):
        self.driver = driver
        self.txtName = (By.XPATH, '//input[@id="name"]')
        self.txtEmail = (By.XPATH, '//input[@id="email"]')
        self.txtPassword = (By.XPATH, '//input[@id="password"]')
        self.txtConfirmPassword = (By.XPATH, '//input[@id="confirmPassword"]')
        self.btnDangKy = (By.XPATH, '//button[@type="submit"]')

    def set_name(self, name):
        name_field = self.driver.find_element(*self.txtName)
        name_field.clear()
        name_field.send_keys(name)

    def set_email(self, email):
        email_field = self.driver.find_element(*self.txtEmail)
        email_field.clear()
        email_field.send_keys(email)

    def set_password(self, password):
        password_field = self.driver.find_element(*self.txtPassword)
        password_field.clear()
        password_field.send_keys(password)

    def set_confirm_password(self, confirm_password):
        confirm_password_field = self.driver.find_element(*self.txtConfirmPassword)
        confirm_password_field.clear()
        confirm_password_field.send_keys(confirm_password)
    
    def click_button_register(self):
        btnDangKy = self.driver.find_element(*self.btnDangKy)
        btnDangKy.click()