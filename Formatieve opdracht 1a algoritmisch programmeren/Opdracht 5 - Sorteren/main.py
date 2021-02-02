lijst = [3, 2, 8, 4, 6, 7, 5, 9, 10, 1]


def sort(array):

    kleiner = []
    gelijkwaardig = []
    groter = []

    if len(array) > 1:
        pivot = array[0] # hier defineren we de pivot

        for index in array: # voor elke element in array die meegegeven word door de gebruiker

            if index < pivot:
                kleiner.append(index)
            elif index == pivot:
                gelijkwaardig.append(index)
            elif index > pivot:
                groter.append(index)

        return sort(kleiner) + gelijkwaardig + sort(groter)  # we sorteren het terug met de elementen die kleiner gelijkwaardig of groter zijn dan het pivot
    else:
        return array

print(sort(lijst))
