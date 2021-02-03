list = [1, 10, 3, 4, 5, 6, 7, 8, 9]

def count(list, x):
    x = 1
    count = 0
    for i in range(len(list)):
        if list[i] == x:
            count += 1
    return count

def difference(list):

    res = [list[i + 1] - list[i] for i in range(len(list) - 1)]
    return res[0]


def control(list):
    a = count(list, 1)
    b = count(list, 0)
    if a > b:
        if b < 12:
            return True
    return False


print(count(list, 1))
print(difference(list))
print(control(list))
