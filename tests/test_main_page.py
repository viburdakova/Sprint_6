import allure
import pytest

from data import data
from conftest import main_page, driver
from data.data import answer_data


@allure.title("Тесты на проверку вопросов")
@allure.feature("Вопросы о важном")
class TestMainPage:

    @pytest.mark.parametrize("number", list(range(8)))

    def test_question_answer(self, main_page, number):
        with allure.step(f"Проверка вопроса {number}"):
            main_page.click_question(number)
            answer_text = main_page.get_answer_text(number)
            assert answer_text == answer_data[number], f"Ответ для вопроса {number} не совпадает"


