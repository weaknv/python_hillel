import random

list_1 = []
list_2 = []

LIST_SIZE = 5
RANDOM_UPPER_BOUND = 10
for _ in range(0,LIST_SIZE):
    list_1.append(random.randint(0,RANDOM_UPPER_BOUND))
for _ in range(0,LIST_SIZE):
    list_2.append(random.randint(0,RANDOM_UPPER_BOUND))

list_difference = []
for element in list_1:
    if element not in list_2:
        list_difference.append(element)



print('Первый список : ' + str(list_1))
print('Второй список: ' + str(list_2))
print(list_difference)