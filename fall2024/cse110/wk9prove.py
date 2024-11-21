print('Welcome to the Shopping Cart Program!\n')
selection = 0
cart = []
class Item:
    def __init__(self, name, price):
        self.name = name
        self.price = price
while selection != 5:
    selection = int(input('Please select one of the following:\n1. Add item\n2. View Cart\n3. Remove item\n4. Compute Total\n5. Quit\nPlease enter an action: '))
    if selection==1:
        name = input('What item would you like to add? ')
        price = float(input(f'What is the price of \'{name}\'? '))
        cart.append(Item(name,price))
        print(f'\'{name}\' has been added to the cart.\n')
    elif selection==2:
        print('The contents of the shopping cart are:')
        for i,item in enumerate(cart):
            print(f'{i+1}. {item.name} - ${item.price:.2f}')
        print()
    elif selection==3:
        remove = int(input('Which item would you like to remove? '))
        del cart[remove-1]
        print('Item removed.\n')
    elif selection==4:
        total=0
        for item in cart:
            total+=item.price
        print(f'The total price of the items in the shopping cart is ${total:.2f}\n')
    else:
        print('Thank you. Goodbye.')