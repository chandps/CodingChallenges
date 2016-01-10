def isClosing(s):
    if s is ')' or s is '}' or s is ']': return True
    return False


def isNested(s1, s2):
    if s1 is '(' and s2 is ')': return True
    if s1 is '{' and s2 is '}': return True
    if s1 is '[' and s2 is ']': return True
    return False


def solution(S):
    stack = []
    for val in S:
        if len(stack) < 1:
            if isClosing(val):
                return 0
            stack.append(val)
            continue

        if isClosing(val):
            if isNested(stack[len(stack) - 1], val):
                stack.pop()
            else:
                return 0
        else:
            stack.append(val)
    if len(stack) == 0 or len(S) == 0:
        return 1
    return 0
