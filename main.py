from src.api import HH
from src.vacancy import Vacancy
from src.saver import JSONSaver

if __name__ == '__main__':
    hh_api = HH()
    hh_api.load_vacancies('Мафия')
    print(hh_api.vacancies[-1])
    vacancies_list = Vacancy.cast_to_object_list(hh_api.vacancies)
    # print(vacancies_list)
    json_saver = JSONSaver()
    json_saver.add_vacancy(vacancies_list)
    answer = json_saver.get_vacancy('Консультант')
    print(answer)
    json_saver.del_vacancy('Консультант')