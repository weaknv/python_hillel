a = int(input('Введите А '))
b = int(input('Введите B '))
summa = 0
def outer(a, b):
    def inner():
        nonlocal summa
        summa = a + b
        return summa
    inner()
    summa = summa + 5
    print(summa)
outer(a,b)