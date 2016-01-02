def solution(N):
    data = {}
    buff = 0
    for i in range(len(N) - 1, 0, -1):
        if i not in data:
            data[i] = N[i] + buff
        buff = data[i]

    buff = N[0]  # P starts from N[1]
    for i in range(1, len(N)):
        if i == 1:
            res = (abs(buff - data[i]))
        res = min(abs(buff - data[i]), res)
        buff = buff + N[i]
    return res


N = [3, 1, 2, 4, 3]
print(solution(N))
