waarde = int(input("Hoe groot?: "))

def pyramide(num):
      # dit is de oploop van het pyramide
      for waarde in range(0, num): # voor elke waarde in range 0 tot met n ookewel de waarde die gegeven word
           for k in range(0, waarde):
                print("*", end="")
           print("\r")

      # dit is de afloop van het pyramide
      for waarde in range(num, 0 , -1): # voor elke waarde in range n tot met 0 ookewel de waarde die gegeven word
          for k in range(0, waarde):
               print("*", end="")
          print("\r")

      print("\n")

def pyramide_while(num):
    i = 1

    while i < num: # er word gekeken of i kleiner is dan num ookewel de waarde die het gebruiker mee geeft
        print("*" * i)
        i += 1 # hier verhogen we de variable i met 1

    while num > 0: # er word gekeken of num groter is dan 0
        print('*' * num)
        num -= 1 # hier verminderen we de variable num met 1


pyramide(waarde)

pyramide_while(waarde)
