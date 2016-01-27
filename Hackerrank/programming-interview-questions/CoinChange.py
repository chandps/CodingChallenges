def coinChange(M, l):
    global memo
    memo = [0] * (M + 1)
    memo[0] = 0

    for i in range(1, M + 1):
        totalChange = 1
        for coinVal in l:
            if coinVal <= i:
                totalChange += (memo[i - coinVal] + 1)
        memo[i] = totalChange
    print(memo)
    # return getChange(M, l)


def getChange(M, l):
    if memo[M] > -1:
        return memo[M]
    print(memo)
    currentChange = 0
    for coinVal in l:
        if coinVal < M:
            currentChange += getChange(M - coinVal, l)

    memo[M] = currentChange
    return currentChange


def main():
    l = list(map(int, input().split()))
    M, N = l[0], l[1]
    l = list(map(int, input().split()))
    # memo = [0] * M+1
    print(coinChange(M, l))


if __name__ == '__main__':
    main()
