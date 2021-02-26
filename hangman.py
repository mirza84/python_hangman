import random
from words import wordz

kod = []
guessing = []
antal_chanser = 10


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'


def check_if_won():
    if '_' not in kod:
        print(bcolors.OKGREEN + 'You won!' + bcolors.ENDC)


random_word = random.choice(wordz)
print(random_word)

for i in random_word:
    kod.append('_')
print(kod)

while '_' in kod:
    user_input = str(input(bcolors.HEADER + "Guess a letter: " + bcolors.ENDC))
    antal_chanser -= 1
    print(bcolors.OKCYAN +
          f"Antal chanser kvar: {antal_chanser}" + bcolors.ENDC)
    guessing.append(user_input)
    utan_dubbletter = set(guessing)
    print(bcolors.OKBLUE + f"Redan använt: {utan_dubbletter}" + bcolors.ENDC)

    if antal_chanser == 0:
        print(bcolors.FAIL + 'Du förlorade' + bcolors.ENDC)
        break
    elif user_input in kod:
        print(bcolors.WARNING + 'Du har redan använt bokstaven!' + bcolors.ENDC)
    elif user_input not in kod and user_input not in random_word:
        print(bcolors.WARNING + 'Fel bokstav!' + bcolors.ENDC)
        print(kod)
    else:
        counter = 0
        for i in random_word:
            letter = random_word[counter]
            if letter == user_input:
                kod[counter] = letter
                # print(kod)
            counter += 1
        print(kod)
        check_if_won()
