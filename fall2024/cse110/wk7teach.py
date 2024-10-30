import random
again = 'yes'
while again == 'yes':
    magicNumber = random.randint(0,100)
    guess = int(input("What is your guess? "))
    numGuesses=0
    while guess != magicNumber:
        numGuesses+=1
        if guess>magicNumber:
            print('Lower')
        else:
            print('Higher')
        guess = int(input("What is your guess? "))
    again = input(f'You guessed it in {numGuesses} guesses!\nWant to play again? ').lower()
    if again != 'yes':
        print('Okay, bye bye')