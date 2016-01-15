def binsearch(A, x):
    left = 0
    right = len(A) - 1

    while left <= right:
        mid = (left + right) // 2
        if A[mid] == x:
            return mid
        if A[mid] < x:
            left = mid + 1
        elif A[mid] > x:
            right = mid - 1
    return -1


A = [11, 9, 8, 7, 6, 5, 4, 1]
A.sort()
print(A)
print(binsearch(A, 10))
