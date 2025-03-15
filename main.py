from src.api import HH
from src.vacancy import Vacancy

if __name__ == '__main__':
    hh_api = HH()
    hh_api.load_vacancies('Мафия')
    print(hh_api.vacancies[2])
    vacancies_list = Vacancy.cast_to_object_list(hh_api.vacancies)
    print(vacancies_list)