import math

items = int(input("Enter the number of items: "))
boxItems = int(input('Enter the number of items per box: '))

if math.ceil(items/boxItems) > 1:
    print(f'For {items} items, packing {boxItems} in each box, you will need {math.ceil(items/boxItems)} boxes.')
else:
    print(f'For {items} items, packing {boxItems} in each box, you will need {math.ceil(items/boxItems)} box.')