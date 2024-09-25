adjective1 = input('Please enter the following:\n\nadjective: ')
animal = input('animal: ')
verb1 = input('verb: ')
exclamation = input('exclamation: ').capitalize()
verb2 = input('verb: ')
verb3 = input('verb: ')
adjective2 = input('adjective: ').lower()

if adjective2[0] in 'aeiou':
    adjective2 = "an "+adjective2
else:
    adjective2 = "a "+adjective2

print(f'\nYour story is:\n\nThe other day, I was really in trouble. It all started when I saw a very\n{adjective1} {animal} {verb1} down the hallway. \"{exclamation}!\" I yelled. But all\nI could think to do was to {verb2} over and over. Miraculously,\nthat caused it to stop, but not before it tried to {verb3}\nright in front of my family. Needless to say, it was\n{adjective2} day.\n')