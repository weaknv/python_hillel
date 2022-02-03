import random

main_list = []
copy_list = []

LIST_SIZE = 10
RANDOM_UPPER_BOUND = 10
for idx in range(0,LIST_SIZE):
    main_list.append(random.randint(0,RANDOM_UPPER_BOUND))

for _ in main_list:
    copy_list.append(_)

print('Изначальный список : ' + str(main_list))
print('Окончательный список: ' + str(copy_list))