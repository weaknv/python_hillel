import random

list = []
list_without_duplicates = []

LIST_SIZE = 10
RANDOM_UPPER_BOUND = 10
for idx in range(0,LIST_SIZE):
    list.append(random.randint(0,RANDOM_UPPER_BOUND))

for _ in list :
    if _ not in list_without_duplicates:
        list_without_duplicates.append(_)

print('Изначальный список : ' + str(list))
print('Окончательный список: ' + str(list_without_duplicates))