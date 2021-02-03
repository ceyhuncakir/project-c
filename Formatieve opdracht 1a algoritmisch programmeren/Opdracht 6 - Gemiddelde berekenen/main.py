lijst = [1, 2, 3, 4, 5]

lijsten = [[1, 2, 3, 4, 5, 6],[1, 2, 3, 4, 5, 6],[1, 2, 3, 4, 5, 6]]

def gemiddelde_lijst(list):
    return sum(list) / len(list)

def gemiddelde_lijsten(lists):
    average = []
    for i in range(len(lists)):
        average.append(sum(lists[i]) / len(lists[i]))
    return average



print("het gemiddelde is:", gemiddelde_lijst(lijst))
print("het gemiddelde is:", gemiddelde_lijsten(lijsten))
