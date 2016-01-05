def solution(A):
    n = len(A) - 1
    A.sort()
    res = max(A[n] * A[n - 1] * A[n - 2], A[0] * A[1] * A[n])
    return res
