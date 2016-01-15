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


def maxOccurence(A):
    A.sort()
    maxnumber, maxcount, count, lastval = A[0], 0, 0, A[0]

    for i in range(len(A)):
        if lastval == A[i]:
            count += 1
        else:
            lastval = A[i]
            count = 0
        if maxcount < count:
            maxcount = count
            maxnumber = lastval

    return maxnumber, maxcount



A = [2, 3, 2, 3]
print(goldenLeader(A))
A = [1, 2, 3, 4, 5, 5, 5, 5, 3, 2, 1]
print(maxOccurence(A))
