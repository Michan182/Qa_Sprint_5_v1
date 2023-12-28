from faker import Faker
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from locators import Locators

class Test_Registration:
    def test_registration(self, driver):
        self.faker = Faker()
        self.test_name = self.faker.name()
        self.test_email = self.faker.email()
        password = 123456
        driver.find_element(*Locators.PROFILE_BUTTON).click()
        driver.find_element(*Locators.REGISTR_BUTTON).click()
        driver.find_element(*Locators.NAME_REGISTRATION).send_keys(self.test_name)
        driver.find_element(*Locators.EMAIL_REGISTRATION).send_keys(self.test_email)
        driver.find_element(*Locators.PASSWORD_REGISTRATION).send_keys(password)
        driver.find_element(*Locators.SUBMIT_REGISTR_BUTTON).click()

        WebDriverWait(driver, 10).until(
            EC.url_to_be('https://stellarburgers.nomoreparties.site/login'))

        driver.find_element(*Locators.EMAIL_LOGIN).send_keys(self.test_email)
        driver.find_element(*Locators.PASSWORD_LOGIN).send_keys(password)
        driver.find_element(*Locators.PROFILE_BUTTON_ENTER).click()

        WebDriverWait(driver, 10).until(
            EC.url_to_be('https://stellarburgers.nomoreparties.site/'))
        driver.find_element(*Locators.PROFILE_BUTTON).click()

        WebDriverWait(driver, 10).until(
            EC.url_to_be('https://stellarburgers.nomoreparties.site/account/profile'))
        profile_email = driver.find_element(*Locators.PROFILE_EMAIL_FAKE)
        actual_email = profile_email.get_attribute("value")
        expected_email = self.test_email
        assert actual_email == expected_email #проверяем что email пользователя совпадает с зарегистрированным

    def test_incorrect_password_message(self, driver):
        fake = Faker()
        name = fake.name()
        email = fake.email()
        password = "12345"
        driver.find_element(*Locators.PROFILE_BUTTON).click()
        driver.find_element(*Locators.REGISTR_BUTTON).click()
        driver.find_element(*Locators.NAME_REGISTRATION).send_keys(name)
        driver.find_element(*Locators.EMAIL_REGISTRATION).send_keys(email)
        driver.find_element(*Locators.PASSWORD_REGISTRATION).send_keys(password)
        driver.find_element(*Locators.SUBMIT_REGISTR_BUTTON).click()
        incorrect_pass = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(Locators.INCORRECT_PASS_MESSEGE)).text
        assert incorrect_pass == "Некорректный пароль"
