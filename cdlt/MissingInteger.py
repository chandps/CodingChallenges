def solution(A):
    data = [False] * len(A)

    for x in A:
        if 0 < x <= len(A):
            data[x - 1] = True

    for i, x in enumerate(data):
        if x == False:
            return i + 1

    return len(data) + 1
