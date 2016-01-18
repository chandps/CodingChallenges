memo = {}


def fibonacci(n):
    for i in range(n + 1):
        if i == 0:
            memo[i] = 0
        elif i == 1:
            memo[i] = 1
        else:
            memo[i] = memo[i - 1] + memo[i - 2]
    return memo[i]


def main():
    n = int(input())
    print(fibonacci(n))


if __name__ == '__main__':
    main()
