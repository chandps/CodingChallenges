def solution(A):
    val = 0
    for x in A:
        val ^= x
    return val


s = [2, 3, 5, 2, 3]
print(solution(s))
