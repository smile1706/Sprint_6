import allure
from pages.base_page import BasePage

from locators.main_page_locators import MainPageLocators


class MainPage(BasePage):
    @allure.step("Кликнуть на логотип Самокат")
    def click_on_logo_samokat(self):
        self.click_on_element(MainPageLocators.HEADER_LOGO_SAMOKAT)
        self.wait_for_element(MainPageLocators.MAIN_SAMOKAT_IMG)

    @allure.step("Кликнуть на логотип Яндекс")
    def click_on_logo_yandex(self):
        element = self.wait_for_element(MainPageLocators.HEADER_LOGO_YANDEX, 10)
        element.click()

    @allure.step("Ожидание загрузки новой вкладки")
    def new_tab_load_wait(self, url):
        self.redirect_to_new_tab_load_wait(url)