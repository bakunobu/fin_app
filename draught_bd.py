import pandas as pd
import numpy as np
from pymongo import MongoClient


my_client = MongoClient('mongodb://localhost:27017/')

"""
def single_purchase(my_data, my_collection):
    record = my_data.get('Назначение', 'не указано'),
    amt = my_data.get('Сумма', 0),
    tags = my_data.get('Цель', 'не указано'),
    date = my_data.get('Дата', pd.Timestamp.now())
    comment = my_data.get('Комментарий', '')
    try:
        my_collection.insert_one({'Назначение': record,
                                  'Сумма': amt,
                                  'Цель': tags,
                                  'Дата': date,
                                  'Комментарий': comment})
        print(f'Расход на сумму {amt} рублей добавлен!')
    except:
        print('Ошибка! Попробуйте еще раз')
"""

    
def single_purchase(my_data, my_collection):
    try:
        my_collection.insert_one({'Назначение': my_data.get('Назначение', 'не указано'),
                                  'Сумма': my_data.get('Сумма', 0),
                                  'Цель': my_data.get('Цель', 'не указано'),
                                  'Организация': my_data.get('Организация', 0),
                                  'Дата': my_data.get('Дата', pd.Timestamp.now()),
                                  'Комментарий': my_data.get('Комментарий', '')})
        print('Расход на сумму {} рублей добавлен!'.format(my_data.get("Сумма", 0)))
    except:
        print('Ошибка! Попробуйте еще раз')


# testing
# single_purchase(typical_spending, my_client.app_db.budget)

def simple_question(text):
    return(input(text))

def question_math_check(text):
    while True:
        a = simple_question(text)
        try:
            return(float(a))
            break
        except:
            print('Пожалуйста, введите число')

print(question_math_check('Сколько сейчас градусов ниже нуля?'))

# def manual_typein(my_collection):
    