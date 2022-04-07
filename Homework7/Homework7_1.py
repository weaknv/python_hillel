import os.path
import random

NUMBER_UPPER_BOUND = 100
NUMBERS_IN_LINE = 10
LINES_TOTAL_COUNT = 100
FILE_NAME = "randNumbers.txt"

#Test_data
TEST_NUMBERS_IN_LINE = 10
TEST_LINES_TOTAL_COUNT = 100
TEST_NUMBER_UPPER_BOUND = 100


def write_to_file_random_numbers(file_name, numbers_in_line, total_lines, number_upper_bound):
    with open(file_name, 'w') as file:
        for i in range(0, total_lines):
            for n in range(0, numbers_in_line):
                if n == numbers_in_line - 1:
                    file.write(f"{random.randint(0, number_upper_bound)}")
                else:
                    file.write(f"{random.randint(0, number_upper_bound)} ")
            if i != total_lines - 1:
                file.write("\n")


write_to_file_random_numbers(FILE_NAME, NUMBERS_IN_LINE, LINES_TOTAL_COUNT, NUMBER_UPPER_BOUND)



#Tests
def TEST_number_of_numbers_per_line(file_name, numbers_in_line):
    with open(file_name, 'r') as file:
        lines = file.readlines()
        for line in lines:
            assert len(line.split(" ")) == numbers_in_line


def TEST_total_numbers(file_name, total_numbers):
    with open(file_name, 'r') as file:
        lines = file.readlines()
        number_of_lines = len(lines)
        for line in lines:
            assert len(line.split(" ")) * number_of_lines == total_numbers


def TEST_number_of_lines(file_name, lines_count):
    with open(file_name, 'r') as file:
        lines = file.readlines()
        assert len(lines) == lines_count


def TEST_file_exist(file_name):
    assert os.path.exists(file_name)


def TEST_number_upper_bound(file_name, number_upper_bound):
    with open(file_name, 'r') as file:
        lines = file.readlines()
        for line in lines:
            line_list = (line.rstrip().split(" "))
            for num in line_list:
                assert int(num) <= number_upper_bound


TEST_number_of_numbers_per_line(FILE_NAME, TEST_NUMBERS_IN_LINE)
TEST_total_numbers(FILE_NAME, TEST_NUMBERS_IN_LINE*TEST_LINES_TOTAL_COUNT)
TEST_number_of_lines(FILE_NAME, TEST_LINES_TOTAL_COUNT)
TEST_file_exist(FILE_NAME)
TEST_number_upper_bound(FILE_NAME, TEST_NUMBER_UPPER_BOUND)





