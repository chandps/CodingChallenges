def validate(P, Q, R):
    if P + Q > R and Q + R > P and R + P > Q:
        return True
    return False


def solution(A):
    if (len(A) < 2):
        return 0

    A.sort()

    for i in range(len(A) - 2):
        if validate(A[i], A[i + 1], A[i + 2]):
            return 1
    return 0
