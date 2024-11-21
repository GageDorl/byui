print('Please enter the items of the shopping list (type: quit to finish)')
item=''
items=[]
while item!='quit':
    item = input ('Item: ').lower()
    if item!='quit':
        items.append(item.capitalize())
print('\nThe shopping list is:')
for item in items:
    print(item)

print('\nThe shopping list with indexes is:')
for i,item in enumerate(items):
    print(f'{i}. {item}')

index = int(input('\nWhick item would you like to change? '))
newItem = input('What is the new item? ').lower()

items[index] = newItem.capitalize()

print('\nThe shopping list with indexes is:')
for i,item in enumerate(items):
    print(f'{i}. {item}')