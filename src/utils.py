def top_vacancies(vacancies: list[dict], top_n: int, min_pay: int) -> list[dict]:
    """ Функция возвращает заданное количество топ вакансий с указанием минимальной зарплаты"""
    result = [vacancy for vacancy in vacancies if vacancy.get('salary_from') >= min_pay][:top_n]
    result.sort(key=lambda x: x.get('salary_from'), reverse=True)
    return result
