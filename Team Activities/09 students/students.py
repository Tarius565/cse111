import os
import csv

# necessary indexes
I_NUMBER_INDEX = 0
NAME_INDEX = 1

def main():

    path = os.path.abspath(__file__)
    file = os.path.dirname(path)
    
    students_dict = read_dict(f"{file}\students.csv", I_NUMBER_INDEX)

    # print(students_dict)

    number_input = input("Ender the I-Number of the student: ")

    if number_input not in students_dict:
        print("No such student")

    else:
        name = students_dict[number_input]

        print(name)

def read_dict(filename, key_column_index):
    """Read the contents of a CSV file into a compound
    dictionary and return the dictionary.

    Parameters
        filename: the name of the CSV file to read.
        key_column_index: the index of the column
            to use as the keys in the dictionary.
    Return: a compound dictionary that contains
        the contents of the CSV file.
    """
    dictionary = {}

    with open(filename, "rt") as csv_file:

        reader = csv.reader(csv_file)

        next(reader)

        for row_dict in reader:
            if len(row_dict) != 0:
                key = row_dict[key_column_index]
                dictionary[key] = row_dict[NAME_INDEX]

    return dictionary


if __name__ == "__main__":
    main()