def solution(A):
    level = []
    for i, val in enumerate(A):
        level += [(i - val, +1), (i + val, -1)]

    level.sort(key=lambda x: (x[0], -x[1]))

    intersection, active_disk = 0, 0
    for _, elevation in level:
        intersection += active_disk * (elevation > 0)
        active_disk += elevation
        if intersection > 10E6:
            return -1
    return intersection


if __name__ == '__main__':
    print('Start tests..')
    assert solution([1, 2, 1])
    assert solution([1, 5, 2, 1, 4, 0]) == 11
    assert solution([]) == 0
    assert solution([0, 1]) == 1
    assert solution([0, 0]) == 0
    assert solution([1, 0, 0, 3]) == 4
    print('Ok!')
