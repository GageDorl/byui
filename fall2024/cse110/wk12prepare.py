people = [
    "Stephanie 36",
    "John 29",
    "Emily 24",
    "Gretchen 54",
    "Noah 12",
    "Penelope 32",
    "Michael 2",
    "Jacob 10"
]

for i, person in enumerate(people):
    people[i]=person.split(' ')

youngestAge = 100
youngestIndex = -1

for i, person in enumerate(people):
    if int(person[1]) < int(youngestAge):
        youngestAge = person[1]
        youngestIndex = i

print(f'The youngest person is {people[youngestIndex][0]} who is {youngestAge}')