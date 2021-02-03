from random import randrange

def random():
    code = randrange(1, 100)
    print("debug. de code is:", code)

    while True:
        gok = int(input("gok de code: "))

        if gok == code:
            print("je hebt de code goed geraden!. De code was", code)
            break
        else:
            continue

random()
