import csv
from datetime import datetime, timedelta
import random

def main():
    today = datetime.now()
    try:
        products_dict = read_dictionary('products.csv', 0)
    except FileNotFoundError:
        print('File product.csv not found.')
        exit()
    print('Inkom Emporium\n')
    with open('request.csv') as request:
        request = csv.reader(request)
        next(request)
        requestList = []
        countItems = 0
        subtotal = 0
        for line in request:
            try:
                product = products_dict[line[0]]
            except KeyError:
                print(f'Product {line[0]} not found.')
                continue
            print(f'{product[1]}: {line[1]} @ {product[2]}')
            countItems += int(line[1])
            subtotal += int(line[1]) * float(product[2])
            requestList.append(product[1])
        
        print(f'\nNumber of Items: {countItems}')
        print(f'Subtotal: {subtotal:.2f}')
        if(today.time().hour < 11):
            print(f"Before 11 Discount: {subtotal*.01:.2f}")
            subtotal -= subtotal*.01
            print(f'New Subtotal: {subtotal:.2f}')
        elif(today.weekday() == 1 or today.weekday() == 2):
            print(f"{today:%A} Discount: {subtotal*.1:.2f}")
            subtotal -= subtotal*.1
            print(f'New Subtotal: {subtotal:.2f}')
        
        print(f'Tax: {subtotal*.06:.2f}')
        print(f'Total: {subtotal*1.06:.2f}')
        print(f'\nThank you for shopping at Inkom Emporium.')
        print(f'{today:%a %b %d %I:%M:%S %Y}')
        print('\nPlease fill out a survey at www.inkomemporium.com/survey')
        print(f"\nHere's a couppon for {random.choice(requestList)}")
        print(f"Return window ends {today+timedelta(days=7):%b %d %Y}")
        print(f"{(datetime(2026, 1, 1)-today).days} days until the new years sale")

        





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
            dictionaries[line[key_column_index]] = line
        
    return dictionaries

if __name__ == '__main__':
    main()