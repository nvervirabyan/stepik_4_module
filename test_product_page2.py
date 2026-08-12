from .pages.product_page import ProductPage

def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = "https://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/?promo=newYear2019"
    page = ProductPage(browser, link)                 # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес 
    page.open()                                       # открываем страницу
    page.add_product_to_basket()                      # выполняем метод страницы — добавляем товар в корзину
    page.solve_quiz_and_get_code()                    # решаем математическую задачу
    page.is_not_element_present_on_page()             # проверяем, что элемента нет

def test_guest_cant_see_success_message(browser):
    link = "https://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/?promo=newYear2019"
    page = ProductPage(browser, link)                 # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес 
    page.open()                                       # открываем страницу
    page.is_not_element_present_on_page()             # проверяем, что элемента нет

def test_message_disappeared_after_adding_product_to_basket(browser):
    link = "https://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/?promo=newYear2019"
    page = ProductPage(browser, link)                 # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес 
    page.open()                                       # открываем страницу
    page.add_product_to_basket()                      # выполняем метод страницы — добавляем товар в корзину
    page.solve_quiz_and_get_code()                    # решаем математическую задачу
    page.is_disappeared_from_page()                   # проверяем, что элемент пропал
