first = int(input('What is the first number? '))
second = int(input('What is the second number? '))
if(first>second):
    print('The first number is greater\nThe numbers are not equal\nThe second number is not greater\n')
elif(first<second):
    print('The first number is not greater\nThe numbers are not equal\nThe second number is greater\n')
else:
    print('The first number is not greater\nThe numbers are equal\nThe second number is not greater\n')
favorite = str(input('What is your favorite animal? ').lower())
if(favorite=='shark'):
    print('That\'s my favorite animal too!')
else:
    print('That one is not my favorite')