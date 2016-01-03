def solution(X, Y, D):
    jump = (Y - X) // D
    if (jump * D) + X < Y:
        return jump + 1
    return jump

