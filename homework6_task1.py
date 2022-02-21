import random

nums = []

LIST_SIZE = 10
RANDOM_UPPER_BOUND = 100
for _ in range(0,LIST_SIZE):
    nums.append(random.randint(0,RANDOM_UPPER_BOUND))

def buble_sort(l):
    t = l.copy()
    for n in range(0, len(t)):
        for i in range(len(t) - n - 1): #Так мы исключим проверку последнего числа, т.к. оно будет максимальным в конце цикла
            if t[i] > t[i+1]: # Нужно сравнивать числа в теле одного цикла
                t[i], t[i+1] = t[i+1], t[i] # Соответственно и производить их замену тоже.
    return  t

sorted = buble_sort(nums)
print(nums)
print(sorted)

