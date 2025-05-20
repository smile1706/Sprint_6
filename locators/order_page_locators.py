from selenium.webdriver.common.by import By


class OrderPageLocators:
    ORDER_BUTTON = (By.XPATH,"// button[@class='Button_Button__ra12g Button_Middle__1CSJM'][contains(text(), 'Заказать')]")  # кнопка Заказать внизу страницы
    HEADER_ORDER_BUTTON = (By.XPATH, "// button[@class='Button_Button__ra12g'][contains(text(), 'Заказать')]")
    NAME_FIELD = (By.XPATH, "//input[@placeholder='* Имя']")
    SURNAME_FIELD = (By.XPATH, "//input[@placeholder='* Фамилия']")
    ADDRESS_FIELD = (By.XPATH, "//input[@placeholder='* Адрес: куда привезти заказ']")
    STATION_FIELD = (By.XPATH, "//input[@placeholder='* Станция метро']")
    PHONE_FIELD = (By.XPATH, "//input[@placeholder='* Телефон: на него позвонит курьер']")
    DELIVERY_TIME_FIELD = (By.XPATH, "//input[@placeholder='* Когда привезти самокат']")
    RENT_PERIOD_FIELD = (By.XPATH, "//div[@class='Dropdown-placeholder'][contains(text(),'* Срок аренды')]")
    COMMENT_FIELD = (By.XPATH, "//input[@placeholder='Комментарий для курьера']")
    NEXT_ORDER_BUTTON = (By.XPATH, "// button[@class='Button_Button__ra12g Button_Middle__1CSJM'][contains(text(), 'Далее')]")
    FINISH_ORDER_BUTTON = (By.XPATH, "// button[@class='Button_Button__ra12g Button_Middle__1CSJM'][contains(text(), 'Заказать')]")
    POPUP_CONFIRM_BUTTON = (By.XPATH, "// button[@class='Button_Button__ra12g Button_Middle__1CSJM'][contains(text(), 'Да')]")
    POPUP_TRACK_BUTTON = (By.XPATH, "// button[@class='Button_Button__ra12g Button_Middle__1CSJM'][contains(text(), 'Посмотреть статус')]")
    ORDER_PAGE_TITLE = (By.XPATH, "//div[contains(text(), 'Про аренду')]")

    @staticmethod
    def station_metro(number_of_station):
        return By.XPATH, f'//div/ul/li[@data-index="{number_of_station}"]/button'

    @staticmethod
    def rent_period(period):
        return By.XPATH, f'//div[@class="Dropdown-menu"]/div[{period}]'

    @staticmethod
    def samokat_color(color):
        return By.XPATH, f'//label[@for="{color}"]'
