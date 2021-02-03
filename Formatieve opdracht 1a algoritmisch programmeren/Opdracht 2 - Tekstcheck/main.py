s1 = input("Geef een string: ")
s2 = input("Geef een string: ")

def tekstcheck(s1, s2):
    for i in range(0, len(s1)):
        if s1[i] != s2[i]:
            print("Het eerste verschil zit op index: " + str(i))
            break

tekstcheck(s1, s2)
