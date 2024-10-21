def hideThree(thirdPrompt):
    if thirdPrompt == 'check':
        print('The bear is gone, so you leave safely')
    elif thirdPrompt == 'keep':
        print('You keep hiding until you die of dehydration')
    else:
        thirdPrompt = input('You don\'t follow prompts well. Choose CHECK OR KEEP.').lower()
        hideThree(thirdPrompt)

def bearThree(thirdPrompt):
    if thirdPrompt == 'trip':
        print('You trip her and get away safely, but her blood is on your conscience forever.')
    elif thirdPrompt == 'talk':
        print('You try to talk to her but she says "Now is not the time, dude" so you fall over and die of embarassment.')
    elif thirdPrompt == 'run':
        print('You get away safely, and are always left wondering what could have been.')
    else:
        thirdPrompt = input('Nah man. The options were TRIP, TALK, or RUN. Try again.').lower()
        bearThree(thirdPrompt)

def bearTwo(secondPrompt):
    if secondPrompt == 'run':
        thirdPrompt = input('As you\'re running from the bear, you spot a beautiful lady running as well. Do you TRIP her, TALK to her, or RUN the opposite way?').lower()
        bearThree(thirdPrompt)
    elif secondPrompt == 'hide':
        thirdPrompt = input('You hide, and you think your hear the bear walk away. Should you CHECK, or KEEP hiding?').lower()
        hideThree(thirdPrompt)
    else:
        secondPrompt = input('Please choose either RUN or HIDE.').lower()
        bearTwo(secondPrompt)

def wolvesThree(thirdPrompt):
    if thirdPrompt == 'sven':
        print('You and your Svens live happily until your next adventure')
    elif thirdPrompt == 'svenlina':
        print('You and your Svenlinas live happily until your next adventure')
    else:
        thirdPrompt = input('You can only name them Sven or Svenlina, try again.').lower()
        wolvesThree(thirdPrompt)

def badMove(thirdPrompt):
    if thirdPrompt == 'die':
        print('Yeah, there wasn\'t much you could do, you whimper and die.')
    elif thirdPrompt == 'rub':
        print('Really dude?\n\nOkay, you try to rub their bellies and they bit your fingers off before you die')
    else:
        thirdPrompt = input('Nope, too late, you shoud\'ve tamed them brother, now you either DIE or RUB their bellies').lower()
        badMove(thirdPrompt)

def wolvesTwo(secondPrompt):
    if secondPrompt == 'tame':
        thirdPrompt = input('You try to tame them and they take to it easily. What do you name your wolves? SVEN or SVENLINA?').lower()
        wolvesThree(thirdPrompt)
    elif secondPrompt == 'run':
        thirdPrompt = input('Bad move, wolves are fast. They get you and tackle you to the ground. Do you DIE like a man, or RUB the wolves bellies and see what happens?').lower()
        badMove(thirdPrompt)
    else:
        secondPrompt = input('TAME or RUN dude, make the smart decision.').lower()

def decisionOne(firstPrompt):
    if firstPrompt == 'match':
        secondPrompt = input('You pick up the match and strike it, and for an instant, the forest around you is illuminated. You see a large grizzly bear, and then the match burns out. Do you want to RUN, or HIDE behind a tree?').lower()
        bearTwo(secondPrompt)
    elif firstPrompt == 'flashlight':
        secondPrompt = input('You turn on the flashlight as see a pack of wolves. Do you try to TAME them, or RUN away?').lower()
        wolvesTwo(secondPrompt)
    else:
        firstPrompt = input('Your options were MATCH or FLASHLIGHT. Try Again.').lower()
        decisionOne(firstPrompt)

firstPrompt = input('You are walking through a dark forest and find two items: a MATCH and a FLASHLIGHT. Which one do you want to pick up?').lower()
decisionOne(firstPrompt)