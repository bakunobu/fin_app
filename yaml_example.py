import datetime
import pandas as pd
from report_pd_draught import get_dates
import yaml

budget = yaml.load("""
bank:
    frequency: today
    amount: 2000
income:
    frequency: every 2 weeks on Friday
    amount: 1000
rent:
    frequency: every month
    amount: -1500
fun:
    frequency: every week on Friday and Saturday
    amount: -40
                   """)


def build_calendar(budget):
    TODAY = pd.Timestamp.today().normalize()
    END = TODAY + datetime.timedelta(days=365)
    
    
    calendar = pd.DataFrame(index=pd.date_range(start=TODAY,
                                                end=END))
    
    for k, v in budget.items():
        frequency = v.get('frequency')
        amount = v.get('amount')
        dates = get_dates(frequency)
        i = pd.DataFrame(
            data = {k: amount},
            index = pd.DatetimeIndex(pd.Series(dates))
        )
        calendar = pd.concat([calendar, i], axis = 1).fillna(0)
        calendar['total'] = calendar.sum(axis=1)
        calendar['cum_total'] = calendar['total'].cumsum()
        
    return(calendar)