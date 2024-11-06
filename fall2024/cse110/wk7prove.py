import random
from random_word import RandomWords
r = RandomWords()
print('Welcome to the word guessing game!\n')
wordsList = ['nephi','moroni', 'temple','restoration','helaman','monkey','banana', 'nelson']
word = r.get_random_word()
guess=''
secret=''
guesses = 0
for letter in word:
    secret+='_'
while guess!=word:  
    print(f'Your hint is: {secret}')
    guesses+=1
    guess = input('What is your guess? ').lower()
    if len(guess)!=len(word):
        print(f'Sorry, the guess must have {len(word)} letters.\n')
    else:
        secret=''
        for i,letter in enumerate(guess):
            if word.find(letter)!=-1:
                if word[i] == guess[i]:
                    secret += letter.upper()
                
                else:
                    secret+= letter.lower()
            else:
                secret+= '_'
                
        
print(f'Congratulations! You guessed it!\nIt took you {guesses} guesses.')
