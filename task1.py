one_day_path = float(input("Введите километраж пройденный за один день: "))
total_path = float(input("Введите общую длину маршрута в километрах: "))

numbers_of_days = total_path / one_day_path

print("Для прохождения маршрута потребовалось " +str(numbers_of_days) + " дней")