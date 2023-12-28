from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import Locators


class Test_login_main_page:
    def test_login_main_page(self, driver):
        name = "Mikhail"
        email = "teststashenok5@ya.ru"
        password = "123456"
        driver.find_element(*Locators.LOGIN_BUTTON_MAIN_PAGE).click()
        driver.find_element(*Locators.EMAIL_LOGIN).send_keys(email)
        driver.find_element(*Locators.PASSWORD_LOGIN).send_keys(password)
        driver.find_element(*Locators.PROFILE_BUTTON_ENTER).click()

        WebDriverWait(driver, 10).until(
            EC.url_to_be('https://stellarburgers.nomoreparties.site/'))
        driver.find_element(*Locators.PROFILE_BUTTON).click()

        WebDriverWait(driver, 10).until(
            EC.url_to_be('https://stellarburgers.nomoreparties.site/account/profile'))

        profile_email = driver.find_element(*Locators.PROFILE_EMAIL)
        actual_email = profile_email.get_attribute("value")
        expected_email = email
        assert actual_email == expected_email #проверяем что email пользователя совпадает с зарегистрированным
