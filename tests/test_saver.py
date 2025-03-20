from unittest.mock import patch
from src.saver import JSONSaver
from src.vacancy import Vacancy

vacancies_json = [
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


@patch("json.load")
def test_get_from_file(mock_get):
    mock_get.return_value = vacancies_json
    json_saver = JSONSaver("test_empty.json")
    result = json_saver._get_from_file()
    assert result == vacancies_json


def test_get_from_file_empty():
    json_saver = JSONSaver("test_empty.json")
    result = json_saver._get_from_file()
    assert result == []


def test_get_from_file_not_found(capsys):
    json_saver = JSONSaver("invalid_file")
    json_saver._get_from_file()
    message = capsys.readouterr()
    assert message.out.strip() == "Файл не найден"


def test_add_get_del_vacancy():
    vacancy1 = Vacancy("Администратор", "some_url", 50000, 60000, "Москва")
    vacancy2 = Vacancy("Официант", "some_url", 40000, 50000, "Москва")
    json_saver = JSONSaver("test.json")
    json_saver.add_vacancy([vacancy1, vacancy2])
    assert json_saver._get_from_file() == [
        {
            "name": "Администратор",
            "url": "some_url",
            "salary_from": 50000,
            "salary_to": 60000,
            "description": "Москва",
        },
        {"name": "Официант", "url": "some_url", "salary_from": 40000, "salary_to": 50000, "description": "Москва"},
    ]
    assert json_saver.get_vacancy("Официант") == [
        {"name": "Официант", "url": "some_url", "salary_from": 40000, "salary_to": 50000, "description": "Москва"}
    ]
    json_saver.del_vacancy("Официант")
    assert json_saver._get_from_file() == [
        {"name": "Администратор", "url": "some_url", "salary_from": 50000, "salary_to": 60000, "description": "Москва"}
    ]
