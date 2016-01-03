def solution(A):
    val = 0
    for x in A:
        val ^= x
    return val

