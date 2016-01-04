def solution(A, B, K):
    res = 0
    l, r = 0, 0

    l = A // K
    if A % K != 0:
        l += 1

    r = (B // K) + 1
    if r < l:
        return 0
    return r - l
