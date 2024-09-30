kids_meal = float(input('What is the price of a child\'s meal? '))
adult_meal = float(input('What is the price of an adult\'s meal? '))
kids = int(input('How many children are there? '))
adults = int(input('How many adults are there? '))
tax_rate = float(input('What is the sales tax rate? '))/100
tip_perc = float(input('What percent tip do you want to add? '))/100
sub = round((kids*kids_meal)+(adults*adult_meal),2)
tax = round(sub*tax_rate,2)
tip = round((sub+tax)*tip_perc,2)
total = round((sub+tax+tip),2)
print(f'Subtotal: ${sub:.2f}\nSales Tax: ${tax:.2f}\nTip: ${tip:.2f}\nTotal: ${total:.2f}\n')
def try_payment():
    payment = float(input('What is the payment amount? '))
    if payment<total:
        print(f'${payment:.2f} isn\'t enough money')
        try_payment()
    else:
        print(f'Change: ${round(payment-total,2):.2f}')
        
try_payment()