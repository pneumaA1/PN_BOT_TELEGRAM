def get_vacancies_info(data):
    lst = []
    for item in data:
        s = f"Вакансия: <b>{item['name']}</b>\n" \
            f"{item['alternate_url']}"
        lst.append(s)
    return lst