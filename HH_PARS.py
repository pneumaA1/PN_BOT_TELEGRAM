import json

import requests

vacancies_ids = set()
def get_page(page=0):

    params = {
        'text' : 'python',  # Текст фильтра
        'area' : 16,  # Поиск в городе Минск
        'page' : page,  # Индекс страницы поиска на НН
        'per_page' : 10,  # Кол-во вакансий на 1 странице
        'period' : 1
    }

    req = requests.get('https://api.hh.ru/vacancies', params=params)
    data = req.content.decode()  # Декодируем его ответ, чтобы Кириллица отобразилась корректно
    req.close()
    return data


def parse_data():
    lst_objs, new_objs = [], []
    for i in range(5):
        json_data = get_page(i)
        jsObj = json.loads(json_data)
        lst_objs.extend(jsObj['items'])



    for obj in lst_objs:
        # new_objs.append(obj)
         if obj['id'] not in vacancies_ids:
             new_objs.append(obj)
         vacancies_ids.add(obj['id'])

    return new_objs

