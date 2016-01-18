def fizzbuzz(n):
    s = ""
    if n % 3 == 0:
        s += "Fizz"
    if n % 5 == 0:
        s += "Buzz"
    if s == "":
        s = n
    return s


def main():
    n = int(input())
    for i in range(1, n + 1):
        print(fizzbuzz(i))


if __name__ == '__main__':
    main()
