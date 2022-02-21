def isPower2(n):
    return "YES" if (n & (n-1)) == 0 else "NO"
print(isPower2(int(input('Введите число '))))