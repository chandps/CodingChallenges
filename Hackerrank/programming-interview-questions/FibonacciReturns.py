import sys

memo = {}


def fibonacci(n):
    if n < 0:
        return 0

    if n in memo:
        return memo[n]

    if n <= 1:
        memo[n] = n
        return memo[n]

    memo[n] = fibonacci(n - 1) + fibonacci(n - 2)
    return memo[n]


def main():
    for line in sys.stdin:
        i = int(line)
        print(fibonacci(i))


if __name__ == '__main__':
    main()
