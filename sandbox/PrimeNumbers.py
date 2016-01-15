def coins(n):
    result = 0
    coin = [0] * (n + 1)
    for i in range(1, n + 1):
        k = i
        while (k <= n):
            coin[k] = (coin[k] + 1) % 2
            k += i
        result += coin[i]
    return result


def divisors(n):
    i = 1
    div = 0
    while (i * i) < n:
        if n % i == 0:
            div += 2
        i += 1
    if (i * i) == n:
        div += 1
    return div


def primality(n):
    if n == 0:
        return False
    if n == 1:
        return True
    i = 2
    while (i * i) <= n:
        if n % i == 0:
            return False
        i += 1
    return True
