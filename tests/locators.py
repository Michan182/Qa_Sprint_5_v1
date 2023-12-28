from selenium.webdriver.common.by import By

class Locators:
    PROFILE_BUTTON = (By.XPATH, '//p[contains(text(), "Личный Кабинет")]') #селектор кнопки личный кабинет
    REGISTR_BUTTON = (By.XPATH,'//a[contains(text(), "Зарегистрироваться")]') #селектор кнопки зарегистрироваться
    NAME_REGISTRATION = (By.XPATH, '//label[text()="Имя"]/following-sibling::*') #селектор поля ввода имени при регистрации
    EMAIL_REGISTRATION = (By.XPATH, '//label[text()="Email"]/following-sibling::*') #селектор поля почты при регистрации
    PASSWORD_REGISTRATION = (By.XPATH, '//label[text()="Пароль"]/following-sibling::*') #селектор поля пароля при регистрации
    SUBMIT_REGISTR_BUTTON = (By.XPATH, "//button[contains(text(), 'Зарегистрироваться')]") #селектор кнопки регистрации
    INCORRECT_PASS_MESSEGE = (By.XPATH, "//p[contains(text(), 'Некорректный пароль')]") #селектор поп-апа неверного пароля

    PROFILE_NAME_FAKE = (By.XPATH, "//li[1]/div/div/input")
    PROFILE_EMAIL_FAKE = (By.XPATH, "//li[2]/div/div/input")

    EMAIL_LOGIN = (By.XPATH, '//label[text()="Email"]/following-sibling::*') #селектор поля почты при авторизации
    PASSWORD_LOGIN = (By.XPATH, '//input[@name="Пароль"]') #селектор поля пароля при авторизации
    PROFILE_BUTTON_ENTER = (By.XPATH, '//button[contains(text(), "Войти")]') #селектор кнопки входа в аккаунт на странице /login

    PROFILE_NAME = (By.XPATH, '//input[@value="Mikhail"]')#имя профиля в личном кабинете
    PROFILE_EMAIL = (By.XPATH, '//input[@value="teststashenok5@ya.ru"]')#email профиля в личном кабинете

    LOGIN_BUTTON_MAIN_PAGE = (By.XPATH, "//button[text()='Войти в аккаунт']") #селектор кнопки "Войти в аккаунт" на главной странице

    LOGIN_BUTTON_REGISTRATION_PAGE = (By.XPATH, "//a[text()='Войти']") #селектор кнопки перехода к авторизации в форме регистрации
    RESTORE_PASS_BUTTON = (By.XPATH, "//a[text()='Восстановить пароль']") #селектор кнопки восстановления пароля
    RESTORE_CONFIRM_BUTTON = (By.XPATH, "//button[text()='Восстановить']") #селектор кнопки подтверждения восстаглвления пароля

    CONSTRUCTOR_BUTTON = (By.XPATH, "//p[text()='Конструктор']")#селектор кнопки конструктора в личном кабинете

    EXIT_BUTTON = (By.XPATH, "//button[text()='Выход']")#селектор кнопки выхода из аккаунта
    INGREDIENT_BRED_MENU = (By.XPATH, "//span[text()='Булки']")#селектор раздела булки
    INGREDIENT_SOUSE_MENU = (By.XPATH, "//span[text()='Соусы']")#селектор раздела соус
    INGREDIENT_FILING_MENU = (By.XPATH, "//span[text()='Начинки']")  # селектор раздела начинка

    INGREDIENT_BRED_LIST = (By.XPATH, "//h2[text()='Булки']")#селектор булки
    INGREDIENT_SOUSE_LIST = (By.XPATH, "//h2[text()='Соусы']")#селектор соус
    INGREDIENT_FILING_LIST = (By.XPATH, "//h2[text()='Начинки']")  # селектор начинка


