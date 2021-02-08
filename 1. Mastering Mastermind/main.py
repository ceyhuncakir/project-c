from termcolor import colored
from random import randrange
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
    3: 1 = Wit, 2 = Magenta, 3 = Blauw, 4 = Geel, 5 = Groen, 6 = Rood.
    4: Kraak de 4 kleurige code binnen 12 pogingen..\n
    @========================================================@\n
    ''', colors[randrange(5)]))

def type_of_algorithm():
    print(colored('''
    @====================== ALGORITME =======================@\n
    1: Knuth algoritme.
    2: SOON.
    3: SOON.
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
            print("SOON")
        elif option == 2:
            print("SOON")
        elif option == 3:
            print("SOON")
        elif option == 4:
            menu()
        else:
            print("\tKies uit 1, 2, 3 of 4.")


def player_vs_bot():

    rules()

    # Kies 4 willekeurige kleuren.
    code = []
    guess=[]

    for i in range(0,4):
        code.append(randrange(1, 7))
    print(colored("\tDe computer heeft een 4 kleurige code gekozen.\n", "yellow"))
    print(code)

    # checked of de code niet gekraakt is door de codebreaker
    while guess != code:
        global cnt

        if cnt > 11:
            print(colored("\tTeveel pogingen. De computer heeft gewonnen.\n", "red"))
            break
        else:
          cnt += 1
          guess = list(map(int, input("\tPoging {}: ".format(cnt))))
          
          feedback = evalueren(guess, code)

          # Visueel overzicht van gekozen kleuren.
          print("\n\t#",cnt,"|", colored("X ", pins[guess[0]]) + "|", colored("X ", pins[guess[1]]) + "|", colored("X ", pins[guess[2]]) + "|", colored("X ", pins[guess[3]]) + "|", end=" ")

          # Aantal rode en witte pinnen per rij.
          print(colored("R:", "red"), feedback[0], end=", ")
          print("W:", feedback[1], "\n")

        # Alle kleuren zijn goed gegokt.
        if guess == code:
          print(colored("\tGewonnen in:", "green"), cnt, "pogingen! \n\tDe code was:",''.join(map(str, code)))
          print(colored("    @========================================================@\n", "yellow"))
          write_highscore()

def evalueren(guess, code):
    
    # sum op van code en guess
    matches = sum((Counter(code) & Counter(guess)).values()) 
    # rode pins count
    bulls = sum(c == g for c, g in zip(code, guess)) 
    # return van het rode / witte pins
    return bulls, matches - bulls 

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

if __name__ == '__main__':
    menu()
