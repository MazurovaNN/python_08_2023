#2 Дан список повторяющихся элементов. Вернуть список с дублирующимися элементами. 
#В результирующем списке не должно быть дубликатов.

def find_duplicates(lst):
    return list(set([x for x in lst if lst.count(x) > 1]))

lst = [1, 2, 2, 3, 3, 4, 4, 4, 5, 5, 5, 5]
print(find_duplicates(lst))


#3 В большой текстовой строке подсчитать количество встречаемых слов и 
# вернуть 10 самых частых. Не учитывать знаки препинания и регистр символов. 
# За основу возьмите любую статью из википедии или из документации к языку.


import re
from collections import Counter

def top_10_words(text):
    words = re.findall(r'\b\w+\b', text.lower())
    return Counter(words).most_common(10)

text = """Язык программирования Python 3 — это мощный инструмент для создания программ самого 
разнообразного назначения, доступный даже для новичков. С его помощью можно решать задачи различных типов.
Этот сайт призван помочь начинающим научиться программировать на python 3. Также здесь можно подробнее
узнать об особенностях функционирования этого языка.Язык Python обладает некоторыми примечательными
особенностями, которые обуславливают его широкое распространение. Поэтому прежде чем изучать python, 
следует рассказать о его достоинствах и недостатках."""
print(top_10_words(text))

#4 Создайте словарь со списком вещей для похода в качестве ключа и их массой в качестве значения.
#  Определите какие вещи влезут в рюкзак передав его максимальную грузоподъёмность. Достаточно вернуть
#  один допустимый вариант. *Верните все возможные варианты комплектации рюкзака.


def pack_backpack(items, max_weight):
    possible_items = []
    for item, weight in items.items():
        if weight <= max_weight:
            possible_items.append(item)
            max_weight -= weight
    return possible_items

items = {'tent': 5, 'water': 3, 'food': 4, 'clothes': 2, 'first aid kit': 1}
max_weight = 10
print(pack_backpack(items, max_weight)) 