import random

main_list = []

LIST_SIZE = 5
RANDOM_UPPER_BOUND = 10
for idx in range(0,LIST_SIZE):
    main_list.append(random.randint(0,RANDOM_UPPER_BOUND))

def mult(items):
    if len(items)==1:
        return items[0]
    return mult([items[0]]) * mult(items[1:])
print(main_list)
print(mult(main_list))