def solution(l, M, n):
    for i, val in enumerate(l):
        if M > n or M < 1:
            return 'NIL'
        if i == n - M:
            return val


def main():
    M = int(input())
    l = list(map(int, input().split()))
    n = len(l)
    print(solution(l, M, n))


if __name__ == '__main__':
    main()
