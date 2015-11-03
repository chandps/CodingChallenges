N = int(input())

a,b = 0,0
for i in range(N):
    l = list(map(int, input().split()))
    a = a + l[i]
    b = b + l[(N-1)-i]
    
print(abs(a-b))