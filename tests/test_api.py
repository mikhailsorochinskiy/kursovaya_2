from unittest.mock import patch

import pytest

from src.api import HH


@pytest.fixture
def hh_api():
    return HH()


@patch("requests.get")
def test_api_connect_api(mock_result):
    hh = HH()
    mock_result.return_value.status_code = 200
    assert hh.connect_api().status_code == 200


@patch("requests.get")
def test_api_connect_api_error(mock_result):
    hh = HH()
    mock_result.return_value.status_code = 400
    with pytest.raises(ConnectionError):
        hh.connect_api()


@patch("requests.get")
def test_api_load_vacancies(mock_result):
    hh = HH()
    mock_result.return_value.status_code = 200
    mock_result.return_value.json.return_value = {
        "items": [{"id": "1", "name": "Вакансия 1"}, {"id": "2", "name": "Вакансия 2"}]
    }
    hh.load_vacancies("python")
    assert hh.vacancies[:2] == [{"id": "1", "name": "Вакансия 1"}, {"id": "2", "name": "Вакансия 2"}]
