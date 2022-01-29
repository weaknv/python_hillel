number = int(input("Введите трeхзначное число"))
number1 = number%10
number = number // 10
nubmer2 = number%10
number = number//10


print("Сумма цифр числа равна :", number + nubmer2 + number1)
