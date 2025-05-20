from selenium.webdriver.common.by import By


class ImportantQuestionsPageLocators:
    QUESTIONS = (By.CLASS_NAME, "accordion__button")

    @staticmethod
    def question(number):
        return By.ID, f'accordion__heading-{number}'

    @staticmethod
    def answer(number):
        return By.XPATH, f'//div[@id="accordion__panel-{number}"]/p'

