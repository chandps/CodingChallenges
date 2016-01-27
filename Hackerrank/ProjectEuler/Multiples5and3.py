"""
O(n) solution
O(1) space
"""


def mul(n):
    sum = 0
    i = 0
    while i < n:
        sum += i
        diff = min(5 - (i % 5), 3 - (i % 3))
        if i < 5:
            diff = min(5 - i, 3)
        i += diff

    return sum


def main():
    t = int(input())
    for i in range(t):
        n = int(input())
        print(mul(n))


if __name__ == '__main__':
    main()
