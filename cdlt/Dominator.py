def solution(A):
    size = 0
    value = -1
    lastIndex = -1

    for i in range(len(A)):
        if size == 0:
            value = A[i]
            size += 1
            lastIndex = i
        else:
            if A[i] == value:
                size += 1
            else:
                size -= 1

    if size == 0:
        return -1

    count = 0
    for x in A:
        if x == value:
            count += 1
        if count > (len(A) // 2):
            return lastIndex
    return -1
