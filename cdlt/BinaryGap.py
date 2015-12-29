def solution(N):
    n = bin(N)[2::]
    maxC = 0
    count = 0
    enter = False
    for x in n:
        if x == "1":
            if enter is False:
                enter = True
            else:
                if count > maxC:
                    maxC = count
                count = 0
        elif x == "0":
            if enter is True:
                count += 1
    return maxC


def print_solution(N):
    print(bin(N)[2::])
    print(solution(N))


print_solution(561892)
