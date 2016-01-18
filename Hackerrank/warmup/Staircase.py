N = int(input())
for i in range(N):
    space, sharp = ' '*(N-(i+1)), '#'*(i+1)
    print(space + sharp)