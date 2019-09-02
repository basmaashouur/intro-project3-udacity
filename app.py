import time
from random import randint

pause = 2


def printPause(something, sec):
    print(something)
    time.sleep(sec)


def takeInputChecker(frm, to):
    print('PLease enter a number from: ', frm, 'to', to)
    while True:
        choice = int(input())
        if ((choice < frm) or (choice > to)):
            print('please enter a valid choice')
        else:
            break
    return choice


def endInputChecker(choice1, choice2):
    while True:
        choice = input()
        choice = choice.lower()
        if (choice != choice1 and choice != choice2):
            print('please enter a valid choice')
        else:
            break
    return choice


def randomChoices(start, end):
    return randint(start, end)


def die(check):
    if(check):
        printPause("I am going to kill you, you lost", pause)
    else:
        printPause("Hoooraaaay, I won't kill you, you won yaaay", pause)


def niceGhost():
    printPause("I am a nice ghost don't worry I won't hurt you <3", pause)
    printPause("But there is only one chance that I would hurt you", pause)
    printPause("Enter a number from 1 to 10 so you would know:)", pause)
    choice = takeInputChecker(1, 10)
    rand = randomChoices(1, 10)
    if(rand == choice):
        die(True)
    else:
        die(False)


def evilGhost():
    printPause("I am an evil ghost I want to hurt you coz I am evil", pause)
    printPause("But there is only one chance that I wouldn't hurt you", pause)
    printPause("Enter a number from 1 to 10 so you would know:)", pause)
    choice = takeInputChecker(1, 10)
    rand = randomChoices(1, 10)
    if(rand == choice):
        die(False)
    else:
        die(True)


def main():
    printPause('The abandoned house shuddered on the hill,'
               'wishing the morning light would come', pause)
    printPause('All the sooner to warm its weary walls. '
               'It felt so alone, so empty.', pause)
    printPause('You have decided to give it a visit,'
               'now you have two doors, Red door & black door', pause)
    print('\n')
    print('Enter 1 to enter the red door')
    print('Enter 2 to enter the black door')
    choice = takeInputChecker(1, 2)
    rand = randomChoices(1, 2)
    if(choice == rand):
        niceGhost()
    else:
        evilGhost()


if __name__ == '__main__':
    while True:
        main()
        print('\n')
        printPause('Would you like to play again? (Y/n)', pause)
        answer = endInputChecker("y", "n")
        if answer == 'n':
            break
