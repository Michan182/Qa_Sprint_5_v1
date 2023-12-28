from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import Locators


class Test_exit:
    def test_exit_button_personal_account(self, driver):
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

        driver.find_element(*Locators.EXIT_BUTTON).click()

        WebDriverWait(driver, 10).until(
            EC.url_to_be('https://stellarburgers.nomoreparties.site/login'))

        assert driver.current_url == "https://stellarburgers.nomoreparties.site/login"