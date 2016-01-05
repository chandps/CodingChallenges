def solution(A):
    data = []
    A.sort()
    
    prev = 0
    for i in range(len(A)):
        if i == 0:
            data.append(A[i])
            prev = A[i]
        else:
            if A[i] != prev:
                data.append(A[i])
                prev = A[i]

    return len(data)
