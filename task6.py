#Найти корни квадратного уравнения и вывести их на экран, если они есть.
#Если корней нет, то вывести сообщение об этом.
#Конкретное квадратное уравнение определяется коэффициентами a, b, c, которые вводит пользователь.

#D = b2 − 4ac

print("Найдите корни уравнения a*x2+b*x+c=0")
a = float(input("Введите значение a: "))
b = float(input("Введите значение b: "))
c = float(input("Введите значение c: "))
discriminant = b**2 - 4*a*c
print("Дискриминант = " + str(discriminant))
if discriminant < 0:
    print("Корней нет")
elif discriminant == 0:
    x = -b / (2 * a)
    print("x = " + str(x))
else:
    x1 = (-b + discriminant ** 0.5) / (2 * a)
    x2 = (-b - discriminant ** 0.5) / (2 * a)
    print("x1 = " + str(x1))
    print("x2 = " + str(x2))