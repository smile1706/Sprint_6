from selenium.webdriver.common.by import By


class MainPageLocators:
    MAIN_SAMOKAT_IMG = (By.XPATH, "//div/img[@src='/assets/blueprint.png']")
    HEADER_LOGO_SAMOKAT = (By.XPATH, "//a[@class='Header_LogoScooter__3lsAR']")
    HEADER_LOGO_YANDEX = (By.XPATH, "//a[@class='Header_LogoYandex__3TSOI']")