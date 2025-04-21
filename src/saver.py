import json
import os
from abc import ABC, abstractmethod
from json import JSONDecodeError

from src.vacancy import Vacancy

PATH_DIR = os.path.dirname(os.path.dirname(__file__))


class Saver(ABC):
    """ Класс для работы с вакансиями"""

    @abstractmethod
    def add_vacancy(self, vacancies):
        pass

    @abstractmethod
    def get_vacancy(self, pattern):
        pass

    @abstractmethod
    def del_vacancy(self, pattern):
        pass


class JSONSaver(Saver):
    """ Класс для работы с вакансиями в формате json"""

    def __init__(self, filename='vacancies.json'):
        self.__file_path = os.path.join(PATH_DIR, 'data', filename)

    def _write_to_file(self, vacancies_list: list[dict]):
        """ Метод для записи в файл"""
        try:
            with open(self.__file_path, 'w', encoding='utf-8') as file:
                json.dump(vacancies_list, file, ensure_ascii=False, indent=4)
        except FileNotFoundError:
            print('Файл не найден')

    def _get_from_file(self) -> list[dict]:
        """ Метод для получения списка словарей из файла"""
        try:
            with open(self.__file_path, 'r', encoding='utf-8') as f:
                result = json.load(f)
        except FileNotFoundError:
            print('Файл не найден или еще не создан')
            return []
        except JSONDecodeError:
            return []
        else:
            return result

    def add_vacancy(self, vacancies: list[Vacancy]):
        """ Метод для добавления вакансий в файл, проверяющий есть ли такая же вакансия в файле"""
        vacancies_json = self._get_from_file()
        if len(vacancies_json) != 0:
            vacancies_list_dict = [vacancy.to_dict() for vacancy in vacancies if
                                   vacancy.to_dict() not in vacancies_json]
        else:
            vacancies_list_dict = [vacancy.to_dict() for vacancy in vacancies]
        self._write_to_file(vacancies_json + vacancies_list_dict)

    def get_vacancy(self, pattern: str) -> list[dict]:
        """ Метод для получения вакансий с фильтрацией"""
        answer = []
        vacancies = self._get_from_file()
        for vacancy in vacancies:
            for value in vacancy.values():
                if isinstance(value, str):
                    if pattern.lower() in value.lower():
                        answer.append(vacancy)
        return answer

    def del_vacancy(self, pattern: str):
        """ Метод для удаления вакансий из файла с заданным шаблонном"""
        result = []
        vacancies = self._get_from_file()
        for vacancy in vacancies:
            flag = False
            for value in vacancy.values():
                if isinstance(value, str):
                    if pattern.lower() in value.lower():
                        flag = True
                        break
            if not flag:
                result.append(vacancy)
        self._write_to_file(result)
