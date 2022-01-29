n1 = int(input("Введите первое число"))
n2 = int(input("Введите второе число"))
n3 = int(input("Введите третье число"))

max = n1
if n2 > max :
    max = n2
if n3 > max :
    max = n3

print("Максимальное число это:", max)