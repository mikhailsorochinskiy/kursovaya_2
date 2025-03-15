class Vacancy:
    __slots__ = ("name", "alternate_url", "salary_from", "salary_to", "city")

    def __init__(self, name, alternate_url, salary_from, salary_to, city):
        self.name = name
        self.alternate_url = alternate_url
        self.salary_from = salary_from if salary_from is not None else 0
        self.salary_to = salary_to if salary_to is not None else 0
        self.city = city if city else "Не указан"
        self.__validate()

    def __validate(self):
        if not self.name or not self.alternate_url:
            raise ValueError("Название вакансии и URL обязательны.")
        if self.salary_from < 0 or self.salary_to < 0:
            raise ValueError("Зарплата не может быть меньше 0.")
        if self.salary_from > self.salary_to:
            raise ValueError("Минимальная зарплата не может быть больше максимальной.")

    def __str__(self):
        return f"Вакансия: {self.name}, Зарплата {self.salary_from}-{self.salary_to}, город: {self.city}"

    def __lt__(self, other):
        return (self.salary_from + self.salary_to) / 2 < (other.salary_from + other.salary_to) / 2

    def __gt__(self, other):
        return (self.salary_from + self.salary_to) / 2 > (other.salary_from + other.salary_to) / 2

    @classmethod
    def cast_to_object_list(cls, vacancies):
        vacancies_list = []
        for vacancy in vacancies:
            current_vacancy = cls(
                vacancy.get("name"),
                vacancy.get("alternate_url"),
                vacancy.get("salary").get("from") if vacancy.get("salary") else 0,
                vacancy.get("salary").get("to") if vacancy.get("salary") else 0,
                vacancy.get("area").get("name") if vacancy.get("area") else "Не указан город",
            )
            vacancies_list.append(current_vacancy)
        return vacancies_list
