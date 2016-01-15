def goldenMaxSlice(A):
    max_sum, max_slice = 0, 0
    for val in A:
        max_sum = max(0, max_sum + val)
        max_slice = max(max_slice, max_sum)
    return max_slice
