"""
naive fibonacci
"""
def fibNaive(n):
    if n <= 2: f = 1
    else: f = fibNaive(n - 1) + fibNaive(n - 2)
    return f

"""
memoization fibonacci
"""
memo = {}
def fib(n):
    if n in memo: return memo[n]
    if n <= 2: f = 1
    else: f = fib(n - 1) + fib(n - 2)
    memo[n] = f
    return f

"""
bottom-up fibonacci
"""
memo = {}
def fibBottomUp(n):
    for k in range(n):
        if k<=2: f = 1
        else: f = memo[k-1] + memo[k-2]
        memo[k] = f
    return memo[n]
