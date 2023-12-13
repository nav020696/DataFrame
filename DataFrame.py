"""
В ячейке ниже представлен код генерирующий DataFrame, которая состоит всего из 1 столбца. 
Ваша задача перевести его в one hot вид. Сможете ли вы это сделать без get_dummies?
import random
lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI':lst})
data.head()
"""

import random
import pandas as pd

#Генерация DataFrame
lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI':lst})
print(data)

#Перевод в one hot вид
un_values = data['whoAmI'].unique() #берем уникальные значения из столбца
new_data  = pd.DataFrame(0, index=data.index, columns=un_values) 
for el in un_values:
    new_data.loc[data['whoAmI'] == el, el] = 1

print(new_data)