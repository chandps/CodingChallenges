N = int(input())
l = list(map(int, input().split()))
count = [0,0,0] # count for positive, negative, zero numbers

for x in l:
    if x > 0:
        count[0] += 1
    elif x == 0:
        count[2] += 1
    else:
        count[1] += 1
        
for y in count:
    print('%.3f' % (y/N))