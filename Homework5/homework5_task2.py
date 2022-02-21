import random

list_1 = []
LIST_SIZE = 5
RANDOM_UPPER_BOUND = 10
for _ in range(0,LIST_SIZE):
    list_1.append(random.randint(0,RANDOM_UPPER_BOUND))
print(list_1)
def sum(list_1):
    total = 0
    for x in list_1:
        total += x
    return total
print(sum(list_1))