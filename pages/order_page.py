import allure
from pages.base_page import BasePage
from locators.order_page_locators import OrderPageLocators


class OrderPage(BasePage):
    @allure.step("Кликнуть на кнопку Заказать вверху страницы")
    def click_on_header_order_button(self):
        self.click_on_element(OrderPageLocators.HEADER_ORDER_BUTTON)

    @allure.step("Кликнуть на кнопку Заказать внизу страницы")
    def click_on_order_button(self):
        self.scroll_to_element(OrderPageLocators.ORDER_BUTTON)
        self.click_on_element(OrderPageLocators.ORDER_BUTTON)

    @allure.step("Заполнить форму заказа (часть 1 - Для кого самокат)")
    def fill_order_form_first_part(self, name, surname, address, phone_number):
        self.send_keys_to_input(OrderPageLocators.NAME_FIELD, name)
        self.send_keys_to_input(OrderPageLocators.SURNAME_FIELD, surname)
        self.send_keys_to_input(OrderPageLocators.ADDRESS_FIELD, address)
        self.send_keys_to_input(OrderPageLocators.PHONE_FIELD, phone_number)

    @allure.step("Выбрать станцию метро")
    def select_station(self, station_metro):
        self.click_on_element(OrderPageLocators.STATION_FIELD)
        station_locator = OrderPageLocators.station_metro(station_metro)
        self.scroll_to_element(station_locator)
        self.click_on_element(station_locator)

    @allure.step("Переход ко второй части формы")
    def click_order_form_next_part_button(self):
        self.click_on_element(OrderPageLocators.NEXT_ORDER_BUTTON)

    @allure.step("Заполнить форму заказа (часть 2 - Про аренду)")
    def fill_order_form_second_part(self, date, comment):
        self.send_keys_to_input(OrderPageLocators.DELIVERY_TIME_FIELD, date)
        self.click_on_element(OrderPageLocators.ORDER_PAGE_TITLE)
        self.send_keys_to_input(OrderPageLocators.COMMENT_FIELD, comment)

    @allure.step("Выбрать цвет самоката")
    def select_color(self, samokat_color):
        samokat_color_locator = OrderPageLocators.samokat_color(samokat_color)
        self.scroll_to_element(samokat_color_locator)
        self.click_on_element(samokat_color_locator)

    @allure.step("Выбрать срок аренды")
    def select_rent_period(self, rent_period):
        self.click_on_element(OrderPageLocators.RENT_PERIOD_FIELD)
        rent_period_locator = OrderPageLocators.rent_period(rent_period)
        self.scroll_to_element(rent_period_locator)
        self.click_on_element(rent_period_locator)

    @allure.step("Завершение оформления заказа")
    def click_order_form_finish_button(self):
        self.click_on_element(OrderPageLocators.FINISH_ORDER_BUTTON)

    @allure.step("Подтверждение оформления заказа")
    def click_order_form_popup_confirm_button(self):
        self.click_on_element(OrderPageLocators.POPUP_CONFIRM_BUTTON)

    @allure.step("Кнопка просмотра статуса в popup окне")
    def order_form_popup_visible(self):
        return self.wait_for_element(OrderPageLocators.POPUP_TRACK_BUTTON)
