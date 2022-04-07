import os

NUMBER_UPPER_BOUND = 100
NUMBERS_IN_LINE = 10
LINES_TOTAL_COUNT = 100
FILE_NAME = "randNumbers.txt"


#Test_data
TEST_FILE_NAME = "FileForTest.txt"
TEST_NUMBERS_IN_LINE = 10
TEST_LINES_TOTAL_COUNT = 100
TEST_DATA = [1, 2, 3, 4, 5, 6, 7, 8]


def read_from_file(file_name):
    ret = []
    with open(file_name, 'r') as file:
        lines = file.readlines()
        for line in lines:
            line_list = (line.rstrip().split(" "))
            for num in line_list:
                 ret.append(int(num))
    return ret


def square_the_numbers(nums):
    square_ret = []
    for num in nums:
        square_ret.append(num**2)
    return square_ret


def add_separator(file_name):
    with open(file_name, 'a') as file:
        file.write("\n______________________________________________________\n")


def add_numbers_to_file(file_name, data_to_add, numbers_in_line = 10):
    with open(file_name, 'a') as file:
        counter = 0
        for num in data_to_add:
            file.write(f"{num} ")
            counter += 1
            if counter >= numbers_in_line:
                file.write("\n")
                counter = 0


file_data = read_from_file(FILE_NAME)
square_file_data = square_the_numbers(file_data)
add_separator(FILE_NAME)
add_numbers_to_file(FILE_NAME, square_file_data, NUMBERS_IN_LINE)


#Tests
def TEST_add_numbers_to_file(file_name, test_data):
    #clear file
    with open(file_name, 'w') as file:
        file.close()

    #add data to test file
    add_numbers_to_file(file_name, test_data)

    #read data from test file
    with open(file_name, 'r') as file:
        actual = []
        expected = test_data
        data_from_file = file.readline().split(" ")
        data_from_file.pop()
        for el in data_from_file:
            actual.append(int(el))
        assert expected == actual


def TEST_square_the_numbers():
    actual = square_the_numbers([1, 2, 3])
    expected = [1, 4, 9]
    assert expected == actual


def TEST_number_of_lines(file_name, lines_count):
    with open(file_name, 'r') as file:
        lines = file.readlines()
        assert len(lines) == lines_count


def TEST_file_exist(file_name):
    assert os.path.exists(file_name)


def TEST_number_of_numbers_per_line(file_name, lines_count, numbers_in_line):
    with open(file_name, 'r') as file:
        lines = file.readlines()
        for i in range(lines_count + 1, lines_count * 2 + 1):
            assert len(lines[i].rstrip().split(" ")) == numbers_in_line


TEST_add_numbers_to_file(TEST_FILE_NAME, TEST_DATA)
TEST_square_the_numbers()
TEST_number_of_lines(FILE_NAME, LINES_TOTAL_COUNT*2+1)
TEST_file_exist(FILE_NAME)
TEST_number_of_numbers_per_line(FILE_NAME, TEST_LINES_TOTAL_COUNT, TEST_NUMBERS_IN_LINE)


