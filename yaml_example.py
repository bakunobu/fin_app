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