waarde = int(input("geef een waarde: ")) # defineren we de input

def recurssion(i):
   if i <= 1: # word gekeken of i kleiner of gelijkwaardig staat aan 1
       return i
   else:
       return(recurssion(i-1) + recurssion(i-2)) # hier word de recurssion uitgevoerd ookewel de waarde word in sequence gebracht
for i in range(waarde): # hier doen we voor elke waarde in range van waarde
     print(recurssion(i), end=", ")
