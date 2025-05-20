import allure
import pytest

from data import Data
from pages.important_questions_page import ImportantQuestionsPage

class TestImportantQuestions:
    @allure.title("Тест выпадающего списка в разделе Вопросы о важном")
    @pytest.mark.parametrize('number, expected_text', Data.answers)
    def test_question_answers(self, driver, number, expected_text):
        main_page = ImportantQuestionsPage(driver)

        main_page.wait_for_question_list()
        main_page.click_on_question(number)

        assert main_page.check_answers(number, expected_text)
