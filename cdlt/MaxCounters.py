def solution(N, A):
    data = [0] * N
    mx, rem = 0, 0
    for val in A:
        if val == N + 1:
            rem = mx
        else:
            if data[val - 1] < rem:
                data[val - 1] = rem
            data[val - 1] += 1
            mx = max(data[val - 1], mx)

    for i in range(len(data)):
        if data[i] < rem:
            data[i] = rem

    return data
