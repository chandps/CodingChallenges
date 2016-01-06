def solution():
    T = int(input())
    for t in range(T):
        s = input()
        w = input()
        len_s = len(s)
        len_w = len(w)

        w_ord = 0
        sum_ord = [0] * len_s

        prev = 0

        for i in range(len_s):
            sum_ord[i] = ord(s[i]) + prev
            prev = sum_ord[i]

        for i in range(len_w):
            w_ord = ord(w[i]) + w_ord

        res = 0
        for i in range(len_s - (len_w - 1)):
            if i == 0:
                if sum_ord[i + (len_w - 1)] == w_ord:
                    res += 1
            elif sum_ord[i + (len_w - 1)] - sum_ord[i - 1] == w_ord:
                res += 1
        print(res)


solution()
