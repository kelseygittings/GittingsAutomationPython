class LoginPage:
    textbox_username_id = "email"
    textbox_password_id = "password"
    button_login_id = "logIn"
    checkbox_rememberme_class_name = "form__label--custom"
    link_needHelp_id = "forgot-password-link"

    def __init__(self, driver):
        self.driver=driver

    def setUserName(self, username):
        self.driver.find_element_by_id(self.textbox_username_id).clear
        self.driver.find_element_by_id(self.textbox_username_id).send_keys(username)

    def setPassword(self, password):
        self.driver.find_element_by_id(self.textbox_password_id).clear
        self.driver.find_element_by_id(self.textbox_password_id).send_keys(password)

    def clickLogin(self):
        self.driver.find_element_by_id(self.button_login_id).click()

    def clickRememberMe(self):
        self.driver.find_element_by_class_name(self.checkbox_rememberme_class_name).click()

    def clickNeedHelplink(self):
        self.driver.find_element_by_id(self.link_needHelp_id).click()