def sumArray(x):
    sum = 0;
    for i in x:
        sum = sum + i
    return sum

N = int(input())
numbers = list(map(int, input().split()))
print(sumArray(numbers))