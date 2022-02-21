import random

list_1 = []
LIST_SIZE = 5
RANDOM_UPPER_BOUND = 10
for _ in range(0,LIST_SIZE):
    list_1.append(random.randint(0,RANDOM_UPPER_BOUND))

set1 = set(list_1)

print(set1)
number = int(input('Введите число '))
if number in set1:
    print('Данное число является елементом множества')
else:
    print('Данное число не является елементом множества')
