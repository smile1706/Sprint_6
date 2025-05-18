import allure

from curl import dzen_page, main_site
from pages.main_page import MainPage
from pages.order_page import OrderPage

class TestClickLogoSamokat:
    @allure.title("Тест перехода на главную страницу Самоката")
    def test_click_logo_samokat_redirects_main_page(self,driver):
        main_page = MainPage(driver)
        order_page = OrderPage(driver)
        order_page.click_on_header_order_button()
        main_page.click_on_logo_samokat()
        assert driver.current_url == main_site

    @allure.title("Тест перехода на главную страницу Дзен")
    def test_click_logo_yandex_redirects_dzen(self, driver):
        main_page = MainPage(driver)
        main_page.click_on_logo_yandex()
        assert dzen_page in driver.current_url