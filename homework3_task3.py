max_width =  int(input('Введите размер медианы треугольника: '))

for line_number in range(1,max_width+1):
        print("*" * line_number)
for line_number in range(1,max_width+1):
        print("*" * (max_width-line_number)+" "* (line_number*2))
