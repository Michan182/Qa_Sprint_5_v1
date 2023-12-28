from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import Locators

class Test_login:
    def test_button_personal(self, driver):
        name = "Mikhail"
        email = "teststashenok5@ya.ru"
        password = "123456"
        driver.find_element(*Locators.PROFILE_BUTTON).click()
        driver.find_element(*Locators.EMAIL_LOGIN).send_keys(email)
        driver.find_element(*Locators.PASSWORD_LOGIN).send_keys(password)
        driver.find_element(*Locators.PROFILE_BUTTON_ENTER).click()

        WebDriverWait(driver, 10).until(
            EC.url_to_be('https://stellarburgers.nomoreparties.site/'))
        driver.find_element(*Locators.PROFILE_BUTTON).click()

        WebDriverWait(driver, 10).until(
            EC.url_to_be('https://stellarburgers.nomoreparties.site/account/profile'))

        profile_name = driver.find_element(*Locators.PROFILE_NAME)
        actual_name = profile_name.get_attribute("value")
        expected_name = name
        assert actual_name == expected_name #проверяем что имя пользователя совпадает с зарегистрированным
