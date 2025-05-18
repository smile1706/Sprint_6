import allure
from pages.base_page import BasePage
from curl import *
from locators.main_page_locators import MainPageLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class MainPage(BasePage):
    @allure.step("Кликнуть на логотип Самокат")
    def click_on_logo_samokat(self):
        self.click_on_element(MainPageLocators.HEADER_LOGO_SAMOKAT)
        self.wait_for_element(MainPageLocators.MAIN_SAMOKAT_IMG)

    @allure.step("Кликнуть на логотип Яндекс")
    def click_on_logo_yandex(self):
        element = self.wait_for_element(MainPageLocators.HEADER_LOGO_YANDEX, 10)
        element.click()
        WebDriverWait(self.driver, 10).until(lambda d: len(d.window_handles) > 1)
        self.driver.switch_to.window(self.driver.window_handles[1])
        WebDriverWait(self.driver, 25).until(EC.url_contains(dzen_page))

