number_list = []
file_name = 'files/numberFile.txt'


def create_list_of_100_numbers():
    try:
        for i in range(1, 101):
            number_list.append(i)
        return number_list
    except:
        print('Can not create list of 100 numbers')
        return False


def write_numbers_into_the_file(file, number_list):
    try:
        number_file = open(file, 'w')
        # converting list[int] to string for successful writing into the file
        numbers_str = str(number_list)[1:-1]
        number_file.writelines(numbers_str)
        print('Numbers are saved into the file "' + file_name + '" successfully')
        number_file.close()
        return True
    except IOError:
        print('Can not open file "' + file_name + '"')
        return False
    except:
        print('Can not write numbers into the file')
        return False


def read_numbers_from_file(file):
    try:
        number_file = open(file, 'r')
        numbers = number_file.read()
        print('Numbers from file was readed successfully')
        # converting string to list[string]
        numbers = list(numbers.split(", "))
        # converting list[string] to list[int]
        numbers = [int(number) for number in numbers]
        number_file.close()
        return numbers
    except IOError:
        print('Can not open file "' + file_name + '"')
        return False
    except:
        print('Can not read numbers from the file')
        return False


def get_every_second_number_from_list(numbers):
    try:
        print('Getting every second number')
        return numbers[1::2]
    except:
        print('Can not get every second number from list')
        return False


def main():
    generated_list = create_list_of_100_numbers()
    print('Original list of numbers \n', generated_list)
    write_numbers_into_the_file(file_name, generated_list)
    numbers_from_file = read_numbers_from_file(file_name)
    half_of_numbers = get_every_second_number_from_list(numbers_from_file)
    print('Half of numbers from the file "' + file_name + '": \n', half_of_numbers)


if __name__ == '__main__':
    main()