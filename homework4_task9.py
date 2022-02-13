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
set_dif = set_1.difference(set_2)
print('Результат Difference двух множеств', set_dif)

temp_list_1 = []
for x in list_1:
    if x not in temp_list_1:
        temp_list_1.append(x)
list_1 = temp_list_1

temp_list_3 = []
for x in list_2:
    if x not in temp_list_3:
        temp_list_3.append(x)
list_2 = temp_list_3

for i in list_1:
    if i in list_2:
        list_1.remove(i)

temp_list_2 = []
for x in list_1:
    if x not in temp_list_2:
        temp_list_2.append(x)
print('Список после удаления элементов', list_1)
list_1 = temp_list_2
print('Отсортированный от дубликатов список', list_1)
