def goldenLeader(A):
    size = 0
    value = -1

    for i in range(len(A)):
        if size == 0:
            value = A[i]
            size += 1
        else:
            if value == A[i]:
                size += 1
            else:  # value not same
                size -= 1
    if size == 0:
        return -1
    count = 0
    for val in A:
        if val == value:
            count += 1
        if count > (len(A) // 2):
            return value
    return -1


A = [2, 3, 2, 3]
print(goldenLeader(A))
