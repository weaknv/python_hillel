import random

list_1 = []
list_2 = []
LIST_SIZE = 5
RANDOM_UPPER_BOUND = 10
for _ in range(0,LIST_SIZE):
    list_1.append(random.randint(0,RANDOM_UPPER_BOUND))
for _ in range(0,LIST_SIZE):
    list_2.append(random.randint(0,RANDOM_UPPER_BOUND))

set1 = set(list_1)
set2 = set(list_2)
print(set1)
print(set2)

inter_set = set1.intersection(set2)
if len(inter_set) > 0 :

    print('Два заданных набора (set) имеют общие элементы', inter_set)
else :
    print('Два заданных набора (set)  не имеют общих элементов')