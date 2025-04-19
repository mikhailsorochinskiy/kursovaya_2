import pytest

from src.utils import top_vacancies


@pytest.fixture
def vacancies():
    return [
        {
            "name": "Junior QA (Unity)",
            "url": "https://hh.ru/vacancy/118348382",
            "salary_from": 86207,
            "salary_to": 0,
            "description": "Москва",
        },
        {
            "name": "Начинающий специалист",
            "url": "https://hh.ru/vacancy/118183240",
            "salary_from": 0,
            "salary_to": 0,
            "description": "Минск",
        },
    ]


def test_top_vacancies(vacancies):
    assert top_vacancies(vacancies, 5, 50000) == [
        {
            "name": "Junior QA (Unity)",
            "url": "https://hh.ru/vacancy/118348382",
            "salary_from": 86207,
            "salary_to": 0,
            "description": "Москва",
        }
    ]
