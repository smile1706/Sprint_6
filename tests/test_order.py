import allure
import pytest

from pages.order_page import OrderPage
from helper import *
from data import Credentials


class TestOrderPage:
    @pytest.mark.parametrize(
        'name,surname,address,phone_number,date,comment,period,color',
        [
            ['Александр','Пушкин','Царское Село','89999999999','22.05.2025','Эксперт по дуэлям',4,'grey'],
            ['Зубенко','Михаил','Москва','89991111111','12.06.2025','Мафиозник',2,'black']
        ]
    )

    @allure.title("Тест оформления заказа через кнопку вверху страницы")
    def test_order_header_button(self,driver,name,surname,address,phone_number,date,comment,period,color):
        order_page = OrderPage(driver)
        station_metro = select_metro_station()

        order_page.click_on_header_order_button()
        order_page.fill_order_form_first_part(name, surname, address, phone_number)
        order_page.select_station(station_metro)
        order_page.click_order_form_next_part_button()
        order_page.fill_order_form_second_part(date, comment)
        order_page.select_color(color)
        order_page.select_rent_period(period)
        order_page.click_order_form_finish_button()
        order_page.click_order_form_popup_confirm_button()
        popup = order_page.order_form_popup_visible()

        assert popup.is_displayed()


    @allure.title("Тест оформления заказа через кнопку внизу страницы")
    def test_order_button(self,driver):
        order_page = OrderPage(driver)
        station_metro = select_metro_station()
        credentials = Credentials()

        order_page.click_on_order_button()
        order_page.fill_order_form_first_part(credentials.name, credentials.surname, credentials.address, credentials.phone_number)
        order_page.select_station(station_metro)
        order_page.click_order_form_next_part_button()
        order_page.fill_order_form_second_part(credentials.date, credentials.comment)
        order_page.select_color(credentials.color)
        order_page.select_rent_period(credentials.period)
        order_page.click_order_form_finish_button()
        order_page.click_order_form_popup_confirm_button()
        popup = order_page.order_form_popup_visible()

        assert popup.is_displayed()