from abc import ABC, abstractmethod
import requests


class Parser(ABC):
    """Абстрактный класс для работы с API"""

    @abstractmethod
    def connect_api(self):
        pass

    @abstractmethod
    def load_vacancies(self, keyword: str):
        pass


class HH(Parser):
    """
    Класс для работы с API HeadHunter
    """

    def __init__(self):
        self.__url = 'https://api.hh.ru/vacancies'
        self.__headers = {'User-Agent': 'HH-User-Agent'}
        self._params = {'text': '', 'page': 0, 'per_page': 100}
        self.vacancies = []

    def connect_api(self):
        """ Метод, отправляющий get-запрос и возвращающий объект response"""
        response = requests.get(self.__url, headers=self.__headers, params=self._params)
        if response.status_code != 200:
            raise ConnectionError
        return response

    def load_vacancies(self, keyword: str):
        """ Метод, который забирает вакансии с объекта response и добавляет их в атрибут vacancies"""
        self._params['text'] = keyword
        self._params['per_page'] = 20
        while self._params.get('page') != 20:
            response = self.connect_api()
            vacancies = response.json()['items']
            self.vacancies.extend(vacancies)
            self._params['page'] += 1
