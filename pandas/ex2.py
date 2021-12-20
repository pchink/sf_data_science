import pandas as pd

# Method 1
# Создание dataFrame из словаря, ключи-имена столбцов, значения-списки

countries_df = pd.DataFrame({
    'country': ['Англия', 'Канада', 'США', 'Россия', 'Украина', 'Беларусь', 'Казахстан'],
    'population': [56.29, 38.05, 322.28, 146.24, 45.5, 9.5, 17.04],
    'square': [133396, 9984670, 9826630, 17125191, 603628, 207600, 2724902]
})
countries_df.index = ['UK', 'CA', 'US', 'RU', 'UA', 'BY', 'KZ']
countries_df.population
countries_df.mean(axis=0)

print(countries_df)

# Method 2
# вложенный список, внутрунний список - строки новой таблицы

countries_df = pd.DataFrame(
       data = [
        ['Англия', 56.29, 133396],
        ['Канада', 38.05, 9984670],
        ['США', 322.28, 9826630],
        ['Россия', 146.24, 17125191],
        ['Украина', 45.5, 603628],
        ['Беларусь', 9.5, 207600],
        ['Казахстан', 17.04, 2724902]
    ],
    columns= ['country', 'population', 'square'],
    index = ['UK', 'CA', 'US', 'RU', 'UA', 'BY', 'KZ']
)

print(countries_df)
#display(countries_df)
