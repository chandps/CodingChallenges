def solution(A):
    n = len(A)
    backwards = [0] * n

    buff = 0
    for i in range(n - 1, -1, -1):
        if A[i] == 1:
            backwards[i] = buff + 1
            buff = backwards[i]
        else:
            backwards[i] = buff
    buff = 0
    for i in range(n):
        if buff > 1000000000:
            return -1
        if A[i] == 0:
            buff = buff + backwards[i]

    return buff
