import pytest

from src.vacancy import Vacancy


def test_vacancy_attribute():
    vacancy = Vacancy("Администратор", "some_url", 50000, 60000, "Москва")
    assert vacancy.name == "Администратор"
    assert vacancy.alternate_url == "some_url"
    assert vacancy.salary_from == 50000
    assert vacancy.salary_to == 60000
    assert vacancy.city == "Москва"


def test_salary_is_none():
    vacancy = Vacancy("Администратор", "some_url", None, None, "Москва")
    assert vacancy.salary_from == 0
    assert vacancy.salary_to == 0


def test_vacancy_without_city():
    vacancy = Vacancy("Администратор", "some_url", 50000, 60000, "")
    assert vacancy.city == "Не указан"


def test_validate_name():
    with pytest.raises(ValueError):
        Vacancy("", "", 50000, 60000, "Москва")


def test_validate_url():
    with pytest.raises(ValueError):
        Vacancy("Администратор", "", 70000, 80000, "Москва")


def test_validate_salary_from_under_zero():
    with pytest.raises(ValueError):
        Vacancy("Администратор", "", -10, 60000, "Москва")


def test_validate_salary_to_under_zero():
    with pytest.raises(ValueError):
        Vacancy("Администратор", "", 50000, -10, "Москва")


def test_print_vacancy():
    vacancy = Vacancy("Администратор", "some_url", 50000, 60000, "Москва")
    assert str(vacancy) == "Вакансия: Администратор, Зарплата 50000-60000, город: Москва"


def test_lt_vacancy():
    vacancy1 = Vacancy("Администратор", "some_url", 50000, 60000, "Москва")
    vacancy2 = Vacancy("Официант", "some_url", 40000, 50000, "Москва")
    assert vacancy2 < vacancy1


def test_gt_vacancy():
    vacancy1 = Vacancy("Администратор", "some_url", 50000, 60000, "Москва")
    vacancy2 = Vacancy("Официант", "some_url", 40000, 50000, "Москва")
    assert vacancy1 > vacancy2


def test_cast_to_object_list():
    vacancies_list = [
        {
            "name": "Администратор",
            "alternate_url": "some_url",
            "salary_from": 50000,
            "salary_to": 60000,
            "city": "Москва",
        },
        {"name": "Официант", "alternate_url": "some_url", "salary_from": 40000, "salary_to": 50000, "city": "Москва"},
    ]
    vacancies = Vacancy.cast_to_object_list(vacancies_list)
    assert len(vacancies) == 2
    assert isinstance(vacancies[0], Vacancy)
