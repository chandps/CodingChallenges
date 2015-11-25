def searchInAdjacentNumbers(a, element):
    i = 0
    while i < len(a):
        if a[i] == element:
            return i
        diff = abs(a[i] - element)
        i = i + diff
    return -1

l = [4, 5, 6, 5, 6, 7, 8, 9, 10, 9]
print(searchInAdjacentNumbers(l, 9))
