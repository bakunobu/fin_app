import pandas as pd
import numpy as np
import pymongo
from pymongo import MongoClient
from bson import ObjectId


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
            'Дата': pd.Timestamp(record[4]),
            'Комментарий': record[5]})
    

def manual_input():
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
            'Дата': pd.Timestamp(record[5]),
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

start = pd.Timestamp(2020, 1, 1)
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
    check = collection.find_one(filt)
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

def delete_doc(ID, collection):
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


def get_id(params, my_col):
    document = my_col.find_one(params)
    return(document)


def quiz_taker(num_opt, base_question, reminder):
    '''
    A simple function that prints a question, a reminder
    (and a number of given options in [1-n] format) and checks if the answer is correct
    
    Args:
    =====
    num_opt: int
    a number of options
    
    base_question: str
    the main question
    
    reminder: str
    a short reminder (options and defult step back option will be added automatically)
    
    Returns:
    ========
    answer: int
    a number in a given interval
    '''
    print(base_question)
    while True:
        answer = input(f'{reminder} [1-{num_opt}]\n(0 - return to the previous question):')
        try:
            if int(answer) in range(0, num_opt+1):
                answer = int(answer)
                break
        except:
            print('Wrong input!')
            answer = input(f'please try [1-{num_opt}]\n(0 - return to the previous question):')
    return(answer)

# testing
# a = quiz_taker(2, 'Скажи-ка дядя, ведь недаром \n1. Нет \n2.Да', 'Выберите вариант')




def main():
    # set connection
    my_client = MongoClient('mongodb://localhost:27017/')
    my_col = my_client.app_db.budget
    
    # show main menu
    menu_text ="""
    Please choose an option:
    1) add document
    2) browse through Data Base
    3) reports
    4) find document
    5) edit document
    6) delete
    7) exit
        """
    while True:
        option = quiz_taker(7, menu_text, 'Выберите вариант с помощью клавиатуры')
        
        # exiting option
        if option == 7:
            print('Shutting down...\nBye!')
            break
        
        # do nothing (repeat) option
        elif option == 0:
            continue
        
        # adding new data option
        elif option == 1:
            
            opt = quiz_taker(2,
                       'Выберите характер платежа:\n1) Разовый\n2) Регулярный',
                       'Используйте цифры')
            # return to the previos menu
            if opt == 0:
                continue
            # add single spending
            elif opt == 1:
                single_purchase(manual_input(), my_col)
                print('Information added')
            # add regular spending
            elif opt == 2:
                regular_spending(manual_per_input(), my_col)
                print('Information added')
        # browsing through database
        elif option == 2:
            print('Чаще всего вы тратили деньги на:', end=' ')
            sort_by_count(my_col)
            print('Последние добавленные расходы:')
            return_last(my_col)
            print('This month\'s balance: updating' )
        # reports
        elif option == 3:
            print('Will be here soon')
        
        # search
        elif option == 4:
            
            opt = quiz_taker(2,
                       'Выберите тип поиска:\n1) По дате\n2) По содержанию',
                       'Используйте цифры')
            # return to the previos menu
            if opt == 0:
                continue
            # search by date
            elif opt == 1:
                start = input('Задайте начальную дату (гггг-мм-дд): ')
                end = input('Задайте конечную дату (гггг-мм-дд): ')
                if end:
                    results = find_in_interval(my_col, start, end)
                else:
                    results = find_in_interval(my_col, start)
                if results:
                    print('В указанном интервале найдены следующие записи:')
                    for result in results:
                        print(result)
                else:
                    print('Ничего не найдено')
            # search by field
            elif opt == 2:
                field = input('Выберите поле: ')
                value = input('Выберите значение: ')
                results = simple_search(my_col, field, value)
                if results:
                    print('Найдены следующие записи:')
                    for result in results:
                        print(result)
                else:
                    print('Ничего не найдено')
        # edit document
        elif option == 5:
            field = input('Выберите поле: ')
            value = input('Выберите значение: ')
            upd_field = input('Выберите поле для изменения: ')
            new_value = input('Ввведите новое значение: ')
            if upd_field == 'Дата':
                new_value = pd.Timestamp(new_value)
                
            update_doc(my_col,
                       {field: value},
                       {upd_field: new_value})
            print('Обновлено')
        # delete document
        elif option == 6:
            field = input('Выберите поле: ')
            value = input('Выберите значение: ')
            result = get_id({field: value}, my_col)
            ID =  {'_id': ObjectId(result.get('_id', 'wow'))}
            delete_doc(ID, my_col)
        
        
main()
