import random, time, sys
from termcolor import colored

stuff = []

def add():
    print('')
    stuff.append(input('What Would You Like to Add? -> '))
    print('')
    main()

def remove():
    print('')
    if stuff == []:
        print(colored('There are No Items to Remove!', 'red'))
        print('')
        main()
        return
    for num, i in enumerate(stuff):
        print(f'[{num}] {i}')
    toremove = int(input('What Would You Like to Remove? -> '))
    for num, i in enumerate(stuff):
        if num == toremove:
            stuff.remove(i)
    print('')
    main()

def spin():
    print('')
    if stuff == []:
        print(colored('You Must Add Stuff First!', 'red'))
        print('')
        main()
        return
    random.shuffle(stuff)
    print('')
    print(f'{colored(random.choice(stuff), 'green')} Has Been Chosen.')
    time.sleep(2)
    print('')
    main()


def flip_coin():
    print('')
    print(random.choice(['heads', 'tails']))
    time.sleep(2)
    print('')
    main()

def stop():
    confirmations = ['Y', 'y', '']
    confirm = input('Are You Sure [Y/N]? -> ')
    for i in confirmations:
        if confirm == i:
            sys.exit()
    main()

def main():
    if stuff != []:
        print('Current Wheel:')
        for i in stuff:
            print(colored(i, 'blue'))
        print('')

    actions = {
        'add':add,
        'remove':remove,
        'spin':spin,
        'flip coin':flip_coin,
        'exit':stop,
    }

    try:
        for num, i in enumerate(actions):
            print(f'[{num}] {i}')
    except ValueError:
        print(colored('That is Not An Option!', 'red'))
        main()
        return
    print('')

    todo = int(input('What Would You Like to Do? -> '))

    for num, i in enumerate(actions.values()):
        if todo == num:
            i()
            break

main()
