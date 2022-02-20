def sum_digits(num):
    return num%10 + sum_digits(num//10) if num > 9 else num

print(sum_digits(int(input('Введите число '))))