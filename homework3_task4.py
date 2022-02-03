'''
Даны два целых числа A и В. Выведите все числа от A до B включительно, в порядке возрастания, если A < B, или
в порядке убывания если A > B
'''
a = int(input('Введите A '))
b = int(input('Введите Б '))
if a < b:
    for i in range(a, b + 1):
        print(i)
else:
    for i in range(a, b-1, -1):
        print(i)
