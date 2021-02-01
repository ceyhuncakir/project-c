def fizzbuzz():
    for x in range(1,101):
        if x % 3 == 0 and x % 5 == 0: # hier word er gekeken of de getallen zowel 3 en 5 een veelvoud zijn
            print("FizzBuzz")
        elif x % 3 == 0: # hier word er gekeken of de getallen met een 3 een veelvoud zijn
            print("Fizz")
        elif x % 5 == 0: # hier word er gekeken of de getallen met een 5 een veelvoud zijn
            print("Buzz")
        else:
            print(x) # hier worden de getallen geprint die niet een veelvoud zijn van 3 of 5

fizzbuzz()
