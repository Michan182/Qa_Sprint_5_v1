from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import Locators

class Test_ingredients:
    def test_ingredient_filing(self, driver):

        driver.find_element(*Locators.INGREDIENT_FILING_MENU).click()
        filing = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(Locators.INGREDIENT_FILING_LIST)).text

        actual_value = filing
        expected_value = "Начинки"
        assert actual_value == expected_value

    def test_ingredient_souse(self, driver):

        driver.find_element(*Locators.INGREDIENT_SOUSE_MENU).click()
        souce = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(Locators.INGREDIENT_SOUSE_LIST)).text

        actual_value = souce
        expected_value = "Соусы"
        assert actual_value == expected_value

    def test_ingredient_bred(self, driver):

        driver.find_element(*Locators.INGREDIENT_SOUSE_MENU).click()
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(Locators.INGREDIENT_SOUSE_LIST)) #дополнительный шаг чтобы добраться до булок

        driver.find_element(*Locators.INGREDIENT_BRED_MENU).click()
        bred = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(Locators.INGREDIENT_BRED_LIST)).text

        actual_value = bred
        expected_value = "Булки"
        assert actual_value == expected_value