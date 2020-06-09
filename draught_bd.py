import pandas as pd
import numpy as np
import pymongo
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



def to_dict(record):
    return({'Назначение': record[0],
            'Сумма': record[1],
            'Цель': record[2],
            'Организация': record[3],
            'Дата': record[4],
            'Комментарий': record[5]})
    

def manual_typein():
    record = []
    for _ in ('назначение',
              'сумму',
              'цель',
              'организацию',
              'дату',
              'комментарий'):
        if _ == 'сумму':
            rec = question_math_check(f'укажите {_} платежа: ')
        elif _ == 'комментарий':
            rec = simple_question('Добавьте комментарий к платежу: ')
        else:
            rec = simple_question(f'укажите {_} платежа: ')
        record.append(rec)
    return(to_dict(record))


#  my_rec = manual_typein()
#  testing
#  for k, v in my_rec.items():
#     print(k, v)

# single_purchase(my_rec, my_client.app_db.budget)


def return_last(my_collection):
    return(my_collection.find().sort('Дата',
                                     pymongo.DESCENDING).limit(3))

test_queue = return_last(my_client.app_db.budget)

for _ in test_queue:
    print(_)