import random
print('Welcome to the word guessing game!\n')
wordsList = ['nephi','moroni', 'temple','restoration','helaman','monkey','banana', 'nelson']
word = wordsList[random.randint(0,len(wordsList)-1)]
guess=''
secret=''
correctLetters = []
guesses = 0
for letter in word:
    secret+='_'
while guess!=word:
    
    print(f'Your hint is: {secret}')
    guesses+=1
    guess = input('What is your guess? ').lower()
    if len(guess)!=len(word):
        print('Sorry, the guess must have the same number of letters as the secret word.\n')
    else:
        secret=''
        correct = ''
        for letter in guess:
            if word.find(letter)!=-1:
                if word.find(letter) == guess.find(letter):
                    secret += letter.upper()
                
                else:
                    secret+= letter.lower()
            else:
                secret+= '_'
                
        
print(f'Congratulations! You guessed it!\nIt took you {guesses} guesses.')
