import random, time

stuff = []

def add():
    print('')
    stuff.append(input('What Would You Like to Add? -> '))
    print('')
    main()

def remove():
    print('')
    for num, i in enumerate(stuff):
        print(f'[{num}] {i}')
    toremove = int(input('What Would You Like to Remove? -> '))
    for num, i in enumerate(stuff):
        if num == toremove:
            stuff.remove(i)
    print('')
    main()

def spin():
    random.shuffle(stuff)
    print('')
    print(f'{random.choice(stuff)} Has Been Chosen.')
    time.sleep(2)
    print('')
    main()

def main():
    if stuff != []:
        print('Current Wheel:')
        for i in stuff:
            print(i)
        print('')

    actions = {
        'add':add,
        'remove':remove,
        'spin':spin,
    }

    try:
        for num, i in enumerate(actions):
            print(f'[{num}] {i}')
    except ValueError:
        print('That is Not An Option!')
        main()
        return

    todo = int(input('What Would You Like to Do? -> '))

    for num, i in enumerate(actions.values()):
        if todo == num:
            i()
            break

main()
