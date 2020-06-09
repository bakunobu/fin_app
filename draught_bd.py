import pandas as pd
import numpy as np
from pymongo import MongoClient


my_client = MongoClient('mongodb://localhost:27017/')


typical_spending = {'Назначение': 'Анализы',
                    'Сумма': 360,
                    'Цель': 'Медицина',
                    'Дата': pd.Timestamp.now(),
                    'Комментарий': 'Анализ перед походом к врачу'}


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
        

single_purchase(typical_spending, my_client.app_db.budget)