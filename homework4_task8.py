import random

list_1 = []
list_2 = []
LIST_SIZE = 5
RANDOM_UPPER_BOUND = 10
for _ in range(0,LIST_SIZE):
    list_1.append(random.randint(0,RANDOM_UPPER_BOUND))
for _ in range(0,LIST_SIZE):
    list_2.append(random.randint(0,RANDOM_UPPER_BOUND))
print('Первый список ', list_1)
print('Второй список ', list_2)
set_1 = set(list_1)
set_2 = set(list_2)
set_union = set_1.union(set_2)
print('Результат Union двух множеств', set_union)

for i in list_2:
    list_1.append(i)

temp_list = []
for x in list_1:
    if x not in temp_list:
        temp_list.append(x)
print('Список после объединения', list_1)
list_1 = temp_list
print('Отсортированный от дубликатов список', list_1)

set_1 = set(list_1)
set_2 = set(list_2)
