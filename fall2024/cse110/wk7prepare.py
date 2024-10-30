count=-1
while count <0 :
    count = int(input('Please type a positive number: '))
    if count>=0:
        print(f'The number is: {count}')
    else:
        print('Sorry, that is a negative number. Please try again.')


candy = 'no'
while candy != 'yes':
    candy = input('May I have a piece of candy? ').lower()
print('Thank you.')