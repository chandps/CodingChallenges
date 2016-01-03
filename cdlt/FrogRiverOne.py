def solution(X, A):
    data = {}

    for i, x in enumerate(A):
        if x not in data:
            data[x] = i

    res = 0
    for i in range(1, X + 1):
        if i not in data:
            return -1
        res = max(data[i], res)

    return res
