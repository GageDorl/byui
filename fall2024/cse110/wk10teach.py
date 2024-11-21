class Account:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
accounts = []
print('Enter the names and balances of bank accounts (type: quit when done)')
while True:
    name = input('What is the name of this account? ')
    if name.lower() == 'quit':
        break
    balance = float(input('What is the balance? '))
    accounts.append(Account(name.capitalize(),balance))
print('\nAccount Information: ')
total=0
count=0
largestIndex=0
largest=0
for i, account in enumerate(accounts):
    print(f'{i}. {account.name} - ${account.balance:.2f}')
    total+=account.balance
    count+=1
    if account.balance > largest:
        largest = account.balance
        largestIndex=i
print(f'\nTotal: ${total:.2f}\nAverage: ${total/count:.2f}\nHighest balance: {accounts[largestIndex].name} - ${largest:.2f}')
while True:
    if input('\nDo you want to update an account? ').lower() == 'yes':
        index = int(input('What account index do you want to update? '))
        newBalance = float(input('What is the new amount? '))
        accounts[index].balance = newBalance
        print('\nAccount information: ')
        for i, account in enumerate(accounts):
            print(f'{i}. {account.name} - ${account.balance:.2f}')
    else:
        break
print('\nAccount information: ')
for i, account in enumerate(accounts):
    print(f'{i}. {account.name} - ${account.balance:.2f}')