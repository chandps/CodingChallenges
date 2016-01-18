def uncoupledInt(l):
    res = 0
    for val in l:
        res ^= val
    return res


def main():
    l = list(map(int, input().split(', ')))
    print(uncoupledInt(l))


if __name__ == '__main__':
    main()
