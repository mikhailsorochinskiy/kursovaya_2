from src.api import HH
from src.utils import top_vacancies
from src.vacancy import Vacancy
from src.saver import JSONSaver


hh_api = HH()


def user_interaction():
    """ Функция для общения с пользователем"""
    search_query = input("Введите поисковый запрос: ")
    top_n = int(input("Введите количество вакансий для вывода в топ N: "))
    filter_words = input("Введите ключевые слова для фильтрации вакансий: ")
    min_pay = int(input("Минимальная зарплата от: "))
    hh_api.load_vacancies(search_query)
    vacancies_list = Vacancy.cast_to_object_list(hh_api.vacancies)
    json_saver = JSONSaver()
    json_saver.add_vacancy(vacancies_list)
    filter_vacancies = json_saver.get_vacancy(filter_words)
    top_filter_vacancies = top_vacancies(filter_vacancies, top_n, min_pay)
    print(top_filter_vacancies)
    json_saver.del_vacancy('Консультант')


if __name__ == '__main__':
    user_interaction()
    # hh_api = HH()
    # hh_api.load_vacancies('Мафия')
    # print(hh_api.vacancies[-1])
    # vacancies_list = Vacancy.cast_to_object_list(hh_api.vacancies)
    # # print(vacancies_list)
    # json_saver = JSONSaver()
    # json_saver.add_vacancy(vacancies_list)
    # answer = json_saver.get_vacancy('Консультант')
    # print(answer)
    # json_saver.del_vacancy('Консультант')
