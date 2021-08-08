Финальное задание находится тут - https://github.com/Kolian338/stepik-auto-tests-course/tree/main/stepik_lessons/section4
1. Перейдите в корневую папку проекта и создайте виртуальное окружение с помощью команды: python3 -m venv venv

2. Активируйте окружение: source venv/bin/activate

3. Перед запуском тестов установите пакеты: pip install -r requirements.txt

4. Если возникает ошибка ImportError: attempted relative import with no known parent package, просто удалите точки перед пакетами в файлах с тестами. То есть было "from       .pages.basket_page import BasketPage", должно стать "from pages.basket_page import BasketPage".
