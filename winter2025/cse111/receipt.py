import csv

def main():
    products_dict = read_dictionary('products.csv', 0)
    print('All Products')
    print(products_dict)
    with open('request.csv') as request:
        request = csv.reader(request)
        next(request)
        print('Requested Items')
        for line in request:
            product = products_dict[line[0]]
            print(f'{product[1]}: {line[1]} @ {product[2]}')


def read_dictionary(filename, key_column_index):
    """Read the contents of a CSV file into a compound
    dictionary and return the dictionary.

    Parameters
        filename: the name of the CSV file to read.
        key_column_index: the index of the column
            to use as the keys in the dictionary.
    Return: a compound dictionary that contains
        the contents of the CSV file.
    """
    with open(filename) as dictionary_info:
        dictionary_info = csv.reader(dictionary_info)
        next(dictionary_info)
        dictionaries = {}
        for line in dictionary_info:
            print(line[key_column_index])
            dictionaries[line[key_column_index]] = line
        
    return dictionaries

if __name__ == '__main__':
    main()