word = 'Commitment'
favLetter = input('What is your favorite letter? ').lower()
for letter in word:
    letter = letter.lower()
    if letter == favLetter:
        print('_', end="")
    else:
        print(letter.lower(), end="")
print()
choice = 'yes'
quote = "In coming days, it will not be possible to survive spiritually without the guiding, directing, comforting, and constant influence of the Holy Ghost."
while choice == 'yes':
    num = int(input('Please enter a number: '))
    for i, letter in enumerate(quote):
        # print(i, num)
        if i % num == 0:
            print(letter.upper(), end="")
        else:
            print(letter.lower(), end="")
    print()
    choice = input('Would you like to enter another number? ').lower()
print('Goodbye')