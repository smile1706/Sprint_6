import allure
from pages.base_page import BasePage
from locators.important_questions_page_locators import ImportantQuestionsPageLocators


class ImportantQuestionsPage(BasePage):

    @allure.step("Подождать загрузки списка карточек")
    def wait_for_question_list(self):
        self.wait_for_element(ImportantQuestionsPageLocators.QUESTIONS)

    @allure.step("Открыть вопрос")
    def click_on_question(self, number):
        question_locator = ImportantQuestionsPageLocators.question(number)
        self.scroll_to_element(question_locator)
        self.click_on_element(question_locator)

    @allure.step("Сравнить ответ")
    def check_answers(self, number, expected_text):
        answer_locator = ImportantQuestionsPageLocators.answer(number)
        actual_text = self.get_text_on_element(answer_locator)
        return actual_text == expected_text


