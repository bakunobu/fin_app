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
    last_records = my_collection.find().sort('Дата',
                                     pymongo.DESCENDING).limit(3)
    for record in last_records:
        print(record.get('Назначение', '-'),
              record.get('Сумма', '-'),
              record.get('Дата', '-'), sep=',')

#  testing
# return_last(my_client.app_db.budget)


def sort_by_count(my_collection):
    most_common = my_collection.distinct('Цель')
    print(most_common[0])
   
#  testing    
#  sort_by_count(my_client.app_db.budget)


def regular_spending(my_data, my_collection):
        try:
            my_collection.insert_one({'Назначение': my_data.get('Назначение', 'не указано'),
                                    'Сумма': my_data.get('Сумма', 0),
                                    'Цель': my_data.get('Цель', 'не указано'),
                                    'Организация': my_data.get('Организация', 0),
                                    'Период': my_data.get('Период', 'SM'),
                                    'Дата': my_data.get('Дата', pd.Timestamp.now()),
                                    'Комментарий': my_data.get('Комментарий', '')})
            print('Расход на сумму {} рублей добавлен!'.format(my_data.get("Сумма", 0)))
        except:
            print('Ошибка! Попробуйте еще раз')


def to_dict_reg_pay(record):
    return({'Назначение': record[0],
            'Сумма': record[1],
            'Цель': record[2],
            'Организация': record[3],
            'Период': record[4],
            'Дата': record[5],
            'Комментарий': record[6]})


def manual_per_input():
    record = []
    for _ in ('назначение',
              'сумму',
              'цель',
              'организацию',
              'период',
              'дату',
              'комментарий'):
        if _ == 'сумму':
            rec = question_math_check(f'укажите {_} платежа: ')
        elif _ == 'комментарий':
            rec = simple_question('Добавьте комментарий к платежу: ')
        else:
            rec = simple_question(f'укажите {_} платежа: ')
        record.append(rec)
    return(to_dict_reg_pay(record))

# testing
#  my_rec = manual_per_input()
#  regular_spending(my_rec, my_client.app_db.budget)

start = pd.Timestamp('01-01-2020')
end = pd.Timestamp.today()

#records = my_client.app_db.budget.find({'Дата': {'$lt': end, '$gte': start}})

    

def find_in_interval(my_collection, start, end=pd.Timestamp.now()):
    return(my_collection.find({'Дата': {'$lt': end, '$gte': start}}))

# testing 
# records = find_in_interval(my_client.app_db.budget, start, end)
# for record in records:
#    print(record)


def simple_search(my_collection, field, value):
    return(my_collection.find({field: value}))


# testing
# results = simple_search(my_client.app_db.budget, 'цель', 'подписки')
# for result in results:
#    print(result)


def update_doc(collection, filt, new_data):
    '''
    Updates a document using .find_one_and_update()
    !!!needs an import from bson library!!!
    
    Args:
    =====
    collection: pymongo.collection.Collection class
    a collection to work with
    filter: dict
    a parameter or a set of parameters to find a required document
    new_data: dict
    a new data to update a document with
    
    Returns:
    ========
    None: None type
    Doesn't return anything
    prints 'Document Updated!' if succeded, or error warning if some errors occured.
    
    '''
    check = collection.find_one(params)
    if check:
        try: 
            collection.find_one_and_update(filt,
                                      {'$set': new_data})
            print('Document Updated!')
        except:
            print('Update fail!')
    else:
        print('No such document!')

# testing

def delete_doc(collection, ID):
    '''
    Deletes a document from a collection
    !!!needs an import from bson library!!!

    
    Args:
    =====
    collection: pymongo.collection.Collection class
    a collection to work with
    
    ID: dict
    a parameter or a set of parameters to find a required document
    
    Returns:
    ========
    None: None type
    Doesn't return anything
    prints 'Document Deleted!' if succeded, or 'No such document!'

    '''
    check = collection.find_one(ID)
    
    if check:
        collection.delete_one(ID)
        print('Document Deleted!')
        
    else:
        print('No such document!')
        
# testing
# ID =  {'Title': 'booze'}
# delete_doc(my_client.app_db.budget, ID)
def show_menu():
    print(
        """
Please choose an option:
1) add document
2) browse through Data Base
3) find document
4) edit document
5) delete
6) exit
        """
    )


def main():
    # set connection
    my_client = MongoClient('mongodb://localhost:27017/')
    my_col = my_client.app_db.budget
    
    # show main menu
    show_menu()
    while True:
        print('Bye!')
        break

main()