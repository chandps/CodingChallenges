def solution(A):
    min_index = 0
    min_val = 100001
    for i in range(len(A) - 1):
        if (A[i] + A[i + 1]) / 2.0 < min_val:
            min_val = (A[i] + A[i + 1]) / 2.0
            min_index = i
        if i < len(A) - 2 and (A[i] + A[i + 1] + A[i + 2]) / 3.0 < min_val:
            min_val = (A[i] + A[i + 1] + A[i + 2]) / 3.0
            min_index = i
    return min_index
