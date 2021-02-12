from termcolor import colored
from random import *
import random
from collections import Counter
from itertools import product
import time
from datetime import datetime
import sys
import json

colors = ["green", "blue", "yellow", "red", "cyan"]
pins = ["cyan", "magenta", "white", "blue", "yellow", "green", "red"]
cnt = 0

#TODO Fix: getal hoger dan 6, mag niet (crashed de game). def LIMIT().
#TODO Fix: Witte pin 90% gefixed, ik weet het laatste probleem.
#tempcode = code.copy()
#wanneer die matcht:
#bijv. vervang de matchende pin met een pin "X"
#(of ander symbool dat nooit voorkomt)

def start():

    print(colored('''
    @========================================================@
                         _                      _           _
     _ __ ___   __ _ ___| |_ ___ _ __ _ __ ___ (_)_ __   __| |
    | '_ ` _ \ / _` / __| __/ _ \ '__| '_ ` _ \| | '_ \ / _` |
    | | | | | | (_| \__ \ ||  __/ |  | | | | | | | | | | (_| |
    |_| |_| |_|\__,_|___/\__\___|_|  |_| |_| |_|_|_| |_|\__,_|

    @========================================================@
    ''', colors[randrange(5)]))

def rules():
    print(colored('''
    @====================== SPELREGELS ======================@\n
    1: Rode pin = Kleur komt voor in de code en staat op de juiste plek.
    2: Witte pin = Kleur komt voor in de code, maar staat op de onjuiste plek.
    3: 1 = Magenta, 2 = Wit, 3 = Blauw, 4 = Geel, 5 = Groen, 6 = Rood.
    4: Kraak de 4 kleurige code binnen 12 pogingen..\n
    @========================================================@\n
    ''', colors[randrange(5)]))

def type_of_algorithm():
    print(colored('''
    @====================== ALGORITME =======================@\n
    1: Knuth Algoritme.
    2: Simple Algoritme.
    3: Ozmen Algoritme (Eigen heuristiek).
    4: terug naar main menu\n
    @========================================================@\n
    ''', colors[randrange(5)]))

def game_menu_text():
    print(colored('''
    @====================== GAME MENU =======================@\n
    1 - Speler tegen de computer
    2 - Computer tegen de speler
    3 - Highscore
    4 - Regels
    5 - Sluit\n
    @========================================================@
    ''', colors[randrange(5)]))

def menu():

    start()
    game_menu_text()

    while True:
        option = int(input("\n\tSelecteer gamemode: "))
        if option == 1:
            player_vs_bot()
        elif option == 2:
            algorithm_menu()
        elif option == 3:
            read_highscore()
        elif option == 4:
            rules()
        elif option == 5:
            sys.exit()
        else:
            print("\tKies uit 1, 2, 3, 4 of 5.")

def algorithm_menu():

    type_of_algorithm()

    while True:
        option = int(input("\tSelecteer een optie: "))
        if option == 1:
            code = input("\tGeef een code van 4 nummers op: ")
            knuth_alg(code)
        elif option == 2:
            code = input("\tGeef een code van 4 nummers op: ")
            simple_alg(code)
        elif option == 3:
            code = input("\tGeef een code van 4 nummers op: ")
            ozmen_algoritme(code)
        elif option == 4:
            menu()
        else:
            print("\tKies uit 1, 2, 3 of 4.")

def evalueren(guess, code):
    # alles word opgetelt van code en guess en daar van kan je values pakken
    matches = sum((Counter(code) & Counter(guess)).values())
    # alles opgetelt en gekeken of code gelijkwaardig is aan guess en daarvan worden het bepaald of het bulls zijn of niet
    rode_pins = sum(c == g for c, g in zip(code, guess))
    # rode pins worden gereturned met de matches - rode pins zodat er de witte pins uit komen
    return rode_pins, matches - rode_pins

def print_result(cnt, colorpins, feedback):
    print("\n\t#",cnt,"|", colored("X ", pins[colorpins[0]]) + "|", colored("X ", pins[colorpins[1]]) + "|", colored("X ", pins[colorpins[2]]) + "|", colored("X ", pins[colorpins[3]]) + "|", end=" ")
    print(colored("R:", "red"), feedback[0], end=", ")
    print("W:", feedback[1], "\n")

def colorpins_add(guess, colorpins):
    for item in range(0, len(guess), 1):
        colorpins.append(int(guess[item: item + 1]))

def colorpins_clear(colorpins):
    colorpins.clear()

def player_vs_bot():

    rules()

    # Kies 4 willekeurige kleuren.
    code = []
    guess = []

    #random generated codes die in het lijst worden gezet
    for i in range(0, 4):
        code.append(randrange(1, 7))

    print(colored("\tDe computer heeft een 4 kleurige code gekozen.\n", "yellow"))

    #count
    cnt = 0

    # checked of de code niet gekraakt is door de codebreaker
    while guess != code:

        if cnt == 12:
            print(colored("\tTeveel pogingen. De computer heeft gewonnen.\n", "red"))
            break
        else:
          cnt += 1
          guess = list(map(int, input("\tPoging {}: ".format(cnt))))

          #huidige guess word geevalueert
          feedback = evalueren(guess, code)
          print_result(cnt, guess, feedback)

        # Alle kleuren zijn goed gegokt.
        if guess == code:
          print(colored("\tGewonnen in:", "green"), cnt, "pogingen! \n\tDe code was:",''.join(map(str, code)))
          print(colored("    @========================================================@\n", "yellow"))
          write_highscore()


def knuth_alg(code):

    #codes worden gecreert
    list_codes = [''.join(i) for i in product('123456', repeat=4)]

    #hier word een object callable gemaakt voor het evaluaten voor alle elementen in list_codes
    key = lambda guess: max(Counter(evalueren(guess, code) for code in list_codes).values())
    guess = '1122'

    colorpins = []
    cnt = 1

    while True:
        #huidige feedback van het guess
        feedback = evalueren(guess, code)
        # gaat over de lijst met alle mogelijke cobinaties heen en evalueert alle elementen in het lijst en kijkt of het gelijkwaardig staat aan het huidige guess feedback
        list_codes = [code for code in list_codes if evalueren(guess, code) == feedback]

        colorpins_add(guess, colorpins)

        print_result(cnt, colorpins, feedback)

        colorpins_clear(colorpins)

        # hier word er gekeken of guess gelijkwaardig staat code
        if guess == code:
            print(colored("\tde code was opgelost in:", "green"), cnt, "pogingen! \n\t")
            print(colored("\tde tijd die koste om het code te kraken was:",  "green"), str(round(end - start, 6)), "seconden", "\n\t")
            break

        #hier word er gekeken of er nog een code in het list zit met mogelijke codes
        if len(list_codes) == 1:
            guess = list_codes[0]
            end = time.time()
            cnt += 1
        else:
            #hier voert die het guess uit
            guess = min(list_codes, key=key)
            start = time.time()
            cnt += 1

def simple_alg(code):

    #internal list generated
    list_codes = [''.join(i) for i in product('123456', repeat=4)] # alle mogelijke codes

    guess = '1212'

    colorpins = []
    cnt = 1

    while True:
        #huidige feedback van het guess
        feedback = evalueren(guess, code)
        # gaat over de lijst met alle mogelijke cobinaties heen en evalueert alle elementen in het lijst en kijkt of het gelijkwaardig staat aan het huidige guess feedback
        list_codes = [code for code in list_codes if evalueren(guess, code) == feedback]

        colorpins_add(guess, colorpins)

        print_result(cnt, colorpins, feedback)

        colorpins_clear(colorpins)

        # hier word er gekeken of guess gelijkwaardig staat code
        if guess == code:
            print(colored("\tde code was opgelost in:", "green"), cnt, "pogingen! \n\t")
            break

        #hier word er gekeken of er nog een code in het list zit met mogelijke codes
        if len(list_codes) == 1:
            guess = list_codes[0]
            cnt += 1
        else:
            #hier voert die het guess uit
            guess = list_codes[random.randint(0, random.randint(0, len(list_codes) - 1))]
            cnt += 1

def ozmen_algoritme(code):

    list_codes = [''.join(i) for i in product('123456', repeat=4)] # alle mogelijke codes

    randomgen = []

    #random generated codes die in het lijst worden gezet
    for i in range(0, 4):
        randomgen.append(randrange(1, 7))

    #random code word in het eerste guess gezet
    guess = ''.join([str(elem) for elem in randomgen])

    colorpins = []
    cnt = 1

    while True:
        #huidige feedback van het guess
        feedback = evalueren(guess, code)
        # gaat over de lijst met alle mogelijke cobinaties heen en evalueert alle elementen in het lijst en kijkt of het gelijkwaardig staat aan het huidige guess feedback
        list_codes = [code for code in list_codes if evalueren(guess, code) == feedback]

        colorpins_add(guess, colorpins)

        print_result(cnt, colorpins, feedback)

        colorpins_clear(colorpins)

        # hier wordt er gekeken of guess gelijkwaardig staat code
        if guess == code:
            print(colored("\tde code was opgelost in:", "green"), cnt, "pogingen! \n\t")
            break

        #hier word er gekeken of er nog een code in het list zit met mogelijke codes
        if len(list_codes) == 1:
            guess = list_codes[0]
            cnt += 1
        else:
            #hier voert die het guess uit
            guess = list_codes[-1]
            cnt += 1


def write_highscore():

    save_score = input("\tWil je deze score opslaan (J/N): ").lower()
    all_scores = []

    if save_score == "j":
        username = input("\tVoer een naam in: ")
        all_scores.extend([str(cnt), username, str(datetime.now())])

        with open("highscore.pkl", "ab") as out:
            pickle.dump(all_scores, out)

def read_highscore():

    with open("highscore.pkl", "rb") as file:
        all= pickle.load(file)
        values = " - ".join(map(str, all))
        print("\t", values)

def limit(code):

    try:
        assert str(len(code)) == 4
    except AssertionError:
        print("\n\tVoer precies 4 nummers in.")
        menu()

if __name__ == '__main__':
    menu()
