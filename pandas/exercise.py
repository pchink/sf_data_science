import pandas as pd
countries = pd.Series(
    data = ['Англия', 'Канада', 'США', 'Россия', 'Украина', 'Беларусь', 'Казахстан'],
    index = ['UK', 'CA', 'US', 'RU', 'UA', 'BY', 'KZ'],
    name = 'countries'
)
#display(countries)
print(countries)

#  method 2
countries = pd.Series({
    'UK': 'Англия',
    'CA': 'Канада',
    'US' : 'США',
    'RU': 'Россия',
    'UA': 'Украина',
    'BY': 'Беларусь',
    'KZ': 'Казахстан'},
    name = 'countries'
)
#display(countries)
print(countries)


#доступ к данным в series
print(countries.loc['US'])

#доступ к нескольким данным, оборачиваем в скобки
print(countries.loc[['US', 'RU', 'UK']])

# принимаем на вход порядковый номер элемента Series
print(countries.iloc[6])

# диапазон
print(countries.iloc[1:4])