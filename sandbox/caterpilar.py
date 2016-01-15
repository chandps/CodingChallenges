from collections import deque

"""
1 <= a[i] <= 10E9
"""


def caterpilar(A, s):
    n = len(A)
    head = 0
    total = 0
    for back in range(n):
        while head < n and total + A[head] <= s:
            total += A[head]
            head += 1
        if total == s:
            return True
        total -= A[back]
    return False


def caterpilarList(A, s):
    n = len(A)
    res = deque()
    head = 0
    total = 0
    for back in range(n):
        while head < n and total + A[head] <= s:
            res.append(A[head])
            total += A[head]
            head += 1
        if total == s:
            return res
        total -= A[back]
        if len(res) > 0:
            res.popleft()
    return res


A = [1, 9, 1, 2]

print(caterpilar(A, 10))
print(caterpilarList(A, 10))
