from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import Locators

class Test_restore_pass:
    def test_restore_pass_button(self, driver):
        email = "m.stashenok@yandex.ru"
        driver.find_element(*Locators.PROFILE_BUTTON).click()
        driver.find_element(*Locators.RESTORE_PASS_BUTTON).click()
        driver.find_element(*Locators.EMAIL_LOGIN).send_keys(email)
        driver.find_element(*Locators.RESTORE_CONFIRM_BUTTON).click()

        WebDriverWait(driver, 10).until(
            EC.url_to_be('https://stellarburgers.nomoreparties.site/reset-password'))

        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/reset-password'
