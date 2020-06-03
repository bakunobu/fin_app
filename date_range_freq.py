import pandas as pd


offset_aliases = {'рабочий день': 'B',
                  'будни': 'B',
                  'по будням': 'B',
                  'произвольный рабочий день': 'C',
                  'календарный день': 'D',
                  'каждый день': 'D',
                  'ежедневно': 'D',
                  'каждую неделю': 'W',
                  'еженедельно': 'W',
                  'каждый месяц': 'M',
                  'ежемесячно': 'M',
                  'конец месяца': 'M',
                  'раз в две недели': 'SM',
                  'каждые две недели': 'SM',
                  'в последний рабочий день месяца': 'BM',
                  'задать конец месяца': 'CBM',
                  'в начале месяца': 'SM',
                  'в начале каждого месяца': 'SM',
                  'первого и пятнадцатого числа': 'SMS',
                  'в первый рабочий день месяца': 'BMS',
                  'первый рабочий день месяца': 'BMS',
                  'установить дату начала месяца': 'CBMS',
                  'ежеквартально': 'Q',
                  'в конце квартала': 'Q',
                  'каждый квартал': 'Q',
                  'в последний рабочий день квартала': 'BQ',
                  'в начале квратала': 'QS',
                  'в первый рабочий день квартала': 'BQS',
                  'ежегодно': 'Y',
                  'каждый год': 'Y',
                  'в конце года': 'Y',
                  'в последний рабочий день года': 'BY',
                  'в начале года': 'YS',
                  'в первый рабочий день года': 'BYS',
                  'в рабочие часы': 'BH',
                  'в рабочее время': 'BH',
                  'каждый час': 'H',
                  'ежечасно': 'H',
                  'каждую минуту': 'T',
                  'ежеминутно': 'T',
                  'каждю секунду': 'S',
                  'ежесекундно': 'S',
                  'каждую мс': 'L',
                  'каждую микросекунду': 'U',
                  'каждую наносекунду': 'N'}


anchored_offsets = {'каждое воскресенье': 'W-SUN',
                    'каждый понедельник':'W-MON',
                    'каждый вторник': 'W-TUE',
                    'каждую среду': 'W-WED',
                    'каждый чертверг': 'W-THU',
                    'каждыую пятницу': 'W-FRI',
                    'каждую субботу': 'W-SAT'}


anchored_offsets_q = {'каждый квартал, год кончается в декабре': 'Q-DEC',
                      'каждый квартал, год кончается в январе': 'Q-JAN',
                      'каждый квартал, год кончается в феврале': 'Q-FEB',
                      'каждый квартал, год кончается в марте': 'Q-MAR',
                      'каждый квартал, год кончается в апреле': 'Q-APR',
                      'каждый квартал, год кончается в мае': 'Q-MAY',
                      'каждый квартал, год кончается в июне': 'Q-JUN',
                      'каждый квартал, год кончается в июле': 'Q-JUL',
                      'каждый квартал, год кончается в августе': 'Q-AUG',
                      'каждый квартал, год кончается в сентябре': 'Q-SEP',
                      'каждый квартал, год кончается в октябре': 'Q-OCT',
                      'каждый квартал, год кончается в ноябре': 'Q-NOV'}

anchored_offsets_y = {'каждый год, год кончается в декабре': 'A-DEC',
                      'каждый год, год кончается в январе': 'A-JAN',
                      'каждый год, год кончается в феврале': 'A-FEB',
                      'каждый год, год кончается в марте': 'A-MAR',
                      'каждый год, год кончается в апреле': 'A-APR',
                      'каждый год, год кончается в мае': 'A-MAY',
                      'каждый год, год кончается в июне': 'A-JUN',
                      'каждый год, год кончается в июле': 'A-JUL',
                      'каждый год, год кончается в августе': 'A-AUG',
                      'каждый год, год кончается в сентябре': ' A-SEP',
                      'каждый год, год кончается в октябре': 'A-OCT',
                      'каждый год, год кончается в ноябре': 'A-NOV'}


def freq_rus(phrase, dicts):
    """
    uses a set of abovementioned dicts to find translations
    for freq parameters for pandas.date_range() method
    
    Args:
    =====
    phrase: str
    a freq phrase in Russian
    dicts: iterable
    a list or a tuple with RUS-ENG translation
    
    Returns:
    ========
    freq_phrase: str
    an freq indicator in ENG
    
    OR
    ==
    
    None: None type
    if there's no phrase in a dict
    """
    for my_dict in dicts:
        if phrase.lower() in my_dict.keys():
            return(my_dict[phrase.lower()])


#  testing


#if freq_rus('Каждый год', [offset_aliases]):
#    print(freq_rus('Каждый год', [offset_aliases]))


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



def freq_gen_logic():
    '''
    Эта программа позволяет настраивать частоту для периодов "Квартал" и "Год"
    Доступные опции:
    - период (квартал или год);
    - месяц окончания финансового года (январь-декабрь);
    - наступление события (начало или конец периода);
    - день окончания срока (рабочий или календарный.
    
    Args:
    =====
    No args are required: but you should be ready to type in info during four (or more) input sessions
    
    Returns:
    ========
    freq_tag: str
    a generated (based on ones answers) frequency tag (acronyms are according to pandas manual)
    see: https://pandas.pydata.org/pandas-docs/stable/user_guide/timeseries.html
    '''
    a = 0
    reminder = 'Пожалуйста выберите вариант с помощью клавиатуры'
    while a < 4:
        if a == 0:
            question = 'Пожалуйста, укажите период:\n1. квартал\n2. год'
            period = quiz_taker(2, question, reminder)
            if period == 0:
                a = 0
            else:
                a += 1
        if a == 1:
            question = """
Пожалуйста, укажите месяц окончания финансового года:
1. Январь;
2. Февраль;
3. Март;
4. Апрель;
5. Май;
6. Июнь;
7. Июль;
8. Август;
9. Сентябрь;
10. Октябрь;
11. Ноябрь;
12. декабрь
"""
            year_ends = quiz_taker(12, question, reminder)
            if year_ends == 0:
                a -= 1
            else:
                a += 1
        
        if a == 2:
            question = 'Осуществлять действие в начале или в конце периода:\n1.в начале\n2.в конце'
            start_or_end = quiz_taker(2, question, reminder)
            if start_or_end == 0:
                a -= 1
            elif start_or_end == 1:
                a += 2
                ends_in = 2
            else:
                a += 1
        
        if a == 3:
            question = 'Укажите день окончания срока:\n1.рабочий\n2.календарный'
            ends_in = quiz_taker(2, question, reminder)
            if ends_in == 0:
                a -= 1
            else:
                a += 1
    periods = {1: 'Q',
               2: 'A'}
    
    months = {1: 'JAN',
              2: 'FEB',
              3: 'MAR',
              4: 'APR',
              5: 'MAY',
              6: 'JUN',
              7: 'JUL',
              8: 'AUG',
              9: 'SEP',
              10: 'OCT',
              11: 'NOV',
              12: 'DEC'}
    
    begins = {1: 'S',
              2: ''}
    
    days = {1:'B',
            2: ''}
    
    freq_tag = days[ends_in]+periods[period]+begins[start_or_end]+'-'+months[year_ends]
    return(freq_tag)


# testing
print(freq_gen_logic())