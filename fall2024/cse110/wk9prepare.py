friends = []
friend = ''
while friend.lower() != 'end':
    friend = input('Type the name of a friend: ')
    if friend.lower()!='end':
        friends.append(friend.capitalize())
print('\nYour friends are:')
for friend in friends:
    print(friend)