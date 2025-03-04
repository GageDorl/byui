import re
import csv

def main():
    claimedStudent = input('Enter the I-Number of the studnet you are looking for: ')
    claimedStudent = claimedStudent.replace("-","")
    students = read_dictionary("students.csv", 0)
    if len(claimedStudent) < 9:
        print('Invalid I-Number: too few digits')
    elif len(claimedStudent) > 9:
        print('Invalid I-Number: too many digits')
    elif not re.search(r'^[0-9]{9}$', claimedStudent):
        print('Invalid I-Number: non-numeric characters')
    if claimedStudent in students:
        claimedStudent = students[claimedStudent]
        print(f'The student {claimedStudent['Name']} is in the list.')
    else:
        print(f'No such student')

def read_dictionary(filename, key_column_index):
    with open(filename, "rt") as file:
        reader = csv.reader(file)
        keys = next(reader)
        dictionary = {}
        for row in reader:
            dictionary[row[key_column_index]] = dict(zip(keys, row))
    return dictionary
    # file = open(filename, "r")
    # lines = file.readlines()
    # for i, line in enumerate(lines):
    #     lines[i] = str(line).strip().split(",")
    # file.close()
    # compoundDictionary = {}
    # for i, line in enumerate(lines):
    #     if i == 0:
    #         continue
    #     fields = line
    #     keys = lines[0][0], lines[0][1]
    #     dictionary = {}
    #     for i, key in enumerate(keys):
    #         dictionary[key] = fields[i]
    #         compoundDictionary[fields[key_column_index]] = dictionary  
    # return compoundDictionary
    """Read the contents of a CSV file into a compound
    dictionary and return the dictionary.

    Parameters
        filename: the name of the CSV file to read.
        key_column_index: the index of the column
            to use as the keys in the dictionary.
    Return: a compound dictionary that contains
        the contents of the CSV file.
    """
if __name__ == '__main__':
    main()