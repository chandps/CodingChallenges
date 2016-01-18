def getClosing(c):
    delim = {
        '(': ')',
        '[': ']',
        '{': '}',
    }
    return delim[c]


def delimiters(s):
    opening = []
    for c in s:
        if c in ('(', '[', '{'):
            opening.append(c)
        else:
            if len(opening) == 0:
                return False
            if getClosing(opening.pop()) != c:
                return False
    if len(opening) > 0:
        return False
    return True


def main():
    s = input()
    print(delimiters(s))


if __name__ == '__main__':
    main()
