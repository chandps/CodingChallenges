def sieve(n):
    sieve = [True] * (n + 1)
    sieve[0], sieve[1] = False, False
    i = 2
    while (i * i) <= n:
        if sieve[i]:
            k = i * i
            while (k <= n):
                sieve[k] = False
                k += i
        i += 1
    return sieve


def printSieve(sieveList):
    for i, val in enumerate(sieveList):
        if val == True:
            val = 'Prime'
        else:
            val = 'Composite'
        print(i, val)


def printPrime(sieveList):
    for i, val in enumerate(sieveList):
        if val == True:
            print(i, end=' ')
    print()


if __name__ == '__main__':
    printPrime(sieve(130))
