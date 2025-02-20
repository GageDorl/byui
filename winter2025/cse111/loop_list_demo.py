"""
Use all or any part of this file as a demonstration of iteration (loops)
and lists during class in your section of CSE 111.

You could retain the numbered comments and delete all or any parts of
the code. Then give the modified file to your students and ask them to
write the code for the numbered comments. Or you could write the code
for the numbered comments with them as a demonstration during class.
"""

def main():
    # 1. Write a loop that prints the integers
    # between zero and ten, including zero and ten.
    i = 0
    while i <= 10:
        print(i, end=", ") if i != 10 else print(i)
        i += 1
    print()
    for i in range(11):
        print(i, end=", ") if i != 10 else print(i)
    print()

    # 2. Write a loop that prints the integers
    # between three and ten, including three and ten.
    i = 3
    while i <= 10:
        print(i, end=", ") if i != 10 else print(i)
        i += 1
    print()
    for i in range(3, 11):
        print(i, end=", ") if i != 10 else print(i)
    print()

    # 3. Write a loop that prints the integers 20, 25, 30, 35.
    for i in range(20, 36, 5):
        print(i, end=", ") if i != 35 else print(i)
    print()
    i = 20
    while i <= 35:
        print(i, end=", ") if i != 35 else print(i)
        i += 5
    print()

    # 4. Write a loop that prints the integers 40, 38, 36, 34, 32, 30.
    for i in range(40, 29, -2):
        print(i, end=", ") if i != 30 else print(i)
    print()
    i = 40
    while i > 28:
        print(i, end=", ") if i != 30 else print(i)
        i -= 2
    print()

    # 5. Write a loop that stores the integers from
    # zero to ten in a list. Include zero and ten.
    numbers = []
    for i in range(11):
        numbers.append(i)
    print(numbers)

    # 6. Write a loop that prints each element in a list on a different line.
    people = ["James", "Lisa", "Juan", "Sophia", "William", "Noah", "Olivia"]

    for person in people:
        print(person)

    for i in range(len(people)):
        print(people[i]) if i != 0 else print(f'\n{people[i]}')

    for i, person in enumerate(people):
        print(i+1, person) if i != 0 else print(f'\n{i+1} {person}')

    # Print a blank line.
    print()

    # 7. Below are two parallel lists. Write a loop that prints the elements
    # of both lists to a terminal window on separate lines like this:
    # Ashton 97
    # Chester 75
    # Drummond 83
    # Felt 72
    # Island Park 154
    # Wayan 78
    cities = ["Ashton", "Chester", "Drummond", "Felt", "Island Park", "Wayan"]
    snowfall = [97, 75, 83, 72, 154, 78]  # inches

    for i in range(len(cities)):
        print(cities[i], snowfall[i])
    print()
    zip_cities = zip(cities, snowfall)
    for city, inches in zip_cities:
        print(city, inches)

    # Print a blank line.
    print()



if __name__ == "__main__":
    main()
