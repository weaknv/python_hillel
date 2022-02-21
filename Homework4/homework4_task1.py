import random

list = []

LIST_SIZE = 10
RANDOM_UPPER_BOUND = 10
for idx in range(0,LIST_SIZE):
    list.append(random.randint(0,RANDOM_UPPER_BOUND))

tuple = tuple(list)
print(list)
print(tuple)