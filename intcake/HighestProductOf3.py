def highest_product(l):
    a, b, c = 0, 0, 0
    negativeA, negativeB = 0, 0
    for x in l:
        if x >= 0:
            if x > a:
                c = b
                b = a
                a = x
            elif x > b:
                c = b
                b = x
            elif x > c:
                c = x
        else:
            if x < negativeA:
                negativeB = negativeA
                negativeA = x
            elif x < negativeB:
                negativeB = x

    return a * max(b * c, negativeA * negativeB)

l = [-10, -10, 1, 3, 2]
print(l)
print(highest_product(l))
