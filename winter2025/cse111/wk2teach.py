from datetime import datetime
subtotal=0;
while True:
    price = float(input('What is the price of the item? $'))
    if price:
        quantity = int(input('How many of that item do you have? '))
        subtotal+=price*quantity
    else:
        print(f'Your total is ${subtotal}')
        break
if (datetime.now().weekday() == 1 or datetime.now().weekday() == 2):
    if subtotal>50:
        print(f'Discount amount: ${subtotal*.1:.2f}')
        subtotal=subtotal*.9
    else:
        print(f'If you spend ${50-subtotal:.2f} more then you would save 10%')
salestax = subtotal*.06
print(f'Sales tax amount: ${salestax:.2f}')
print(f'Total: ${subtotal+salestax:.2f}')