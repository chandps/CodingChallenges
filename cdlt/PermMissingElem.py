def solution(A):
    data = [0] * (len(A) + 2)
    for x in A:
        data[x] += 1

    for i in range(1, len(data)):
        if data[i] == 0:
            return i
    return -1


A = [2, 3, 1, 5]
print(solution(A))
