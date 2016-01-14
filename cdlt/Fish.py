def solution(A, B):
    fish = []
    survivor = 0
    for i in range(len(A)):
        if B[i] == 0:
            while len(fish) != 0:
                if fish[-1] < A[i]:
                    fish.pop()
                else:
                    break
            else:
                survivor += 1
        else:
            fish.append(A[i])

    return survivor + len(fish)
