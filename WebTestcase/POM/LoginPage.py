from selenium.webdriver.common.by import By

class LoginPage():
    username=(By.NAME,'accounts')
    password=(By.XPATH,"//*[@type='password']")
    login_button=(By.XPATH,"//*[@type='submit' and text()='登录']")