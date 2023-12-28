Тестирование сайта "https://stellarburgers.nomoreparties.site/" с использованием Selenium и браузера Chrome
Введение
Данный проект представляет собой автоматизированные тесты для веб-приложения "https://stellarburgers.nomoreparties.site/" с использованием библиотеки Selenium и браузера Chrome. Тесты написаны на языке программирования Python с использованием фреймворка pytest.

Установка зависимостей
Установите Python: https://www.python.org/downloads/

Установите необходимые библиотеки, выполнив команду:
pip install -r requirements.txt
Запуск тестов
Перейдите в корневую директорию проекта.

Запустите тесты с помощью следующей команды:

pytest
Структура проекта
tests/
test_button_personal.py: Тесты для кнопок в личном кабинете.
test_constructor_button.py: Тесты для конструктора кнопок.
test_constructor_ingridients.py: Тесты для конструктора ингредиентов.
test_exit_personal_account_button.py: Тесты для кнопки выхода из личного кабинета.
test_login_by_button_personal_account.py: Тесты для входа в личный кабинет через кнопку.
test_login_main_page.py: Тесты для входа с главной страницы.
test_login_restore_pass_button.py: Тесты для восстановления пароля через кнопку.
test_login_through_registration_button.py: Тесты для входа через кнопку регистрации.
test_registration_and_pass_input_error.py: Тесты для ошибок ввода при регистрации и восстановлении пароля.
Обратите внимание
Для успешного запуска тестов убедитесь, что браузер Chrome установлен на вашем устройстве.
Все тесты реализованы с учетом текущего состояния веб-приложения и могут требовать обновлений при изменениях в самом приложении.