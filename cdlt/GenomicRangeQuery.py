def mark_last_seen(S, index, last_seen_type, char):
    if S[index] == char:
        last_seen_type[index] = index
    elif index > 0:
        last_seen_type[index] = last_seen_type[index - 1]


def check_if_char_in_range(P_index, Q_index, last_seen_type):
    if last_seen_type[Q_index] >= P_index:
        return True
    return False


def solution(S, P, Q):
    last_seen_A = [-1] * len(S)
    last_seen_C = [-1] * len(S)
    last_seen_G = [-1] * len(S)
    last_seen_T = [-1] * len(S)

    for i in range(len(S)):
        mark_last_seen(S, i, last_seen_A, 'A')
        mark_last_seen(S, i, last_seen_C, 'C')
        mark_last_seen(S, i, last_seen_G, 'G')
        mark_last_seen(S, i, last_seen_T, 'T')

    res = []
    for i in range(len(Q)):
        if check_if_char_in_range(P[i], Q[i], last_seen_A):
            res.append(1)
        elif check_if_char_in_range(P[i], Q[i], last_seen_C):
            res.append(2)
        elif check_if_char_in_range(P[i], Q[i], last_seen_G):
            res.append(3)
        elif check_if_char_in_range(P[i], Q[i], last_seen_T):
            res.append(4)

    return res
