class Rider:
    def __init__(self, age, height):
        self.age = age
        self.height = height

riders = int(input('Are there 1 or 2 riders? '))

ridersList = []
tooShort = False
canRide = False

for rider in range(riders):
    rider+=1
    age = int(input(f'What is the age of rider number {rider}? '))
    if age<18 and age>=12:
        goldenTicket = input('Do you have a golden pass?(yes or no) ').lower()
        if goldenTicket == 'yes':
            age=18
    height = int(input(f'What is the height in inches of rider number {rider}? '))
    if height<36:
        tooShort = True
    ridersList.append(Rider(age,height))

if len(ridersList)==1:
    if tooShort:
        canRide=False
    elif ridersList[0].age>=18 and ridersList[0].height>=62:
        canRide = True
else:
    if tooShort:
        canRide=False
    elif ridersList[0].age>=18 or ridersList[1].age>=18:
        canRide = True
    elif ridersList[0].age>=12 and ridersList[1].age>=12 and ridersList[0].height>=52 and ridersList[1].height>=52:
        canRide= True
    elif (ridersList[0].age>=16 or ridersList[1].age>=16) and (ridersList[0].age>=14 or ridersList[1].age>=14):
        canRide = True

if canRide:
    print('Welcome to the ride. Please be safe and have fun!')
else:
    print('Sorry, you may not ride.')