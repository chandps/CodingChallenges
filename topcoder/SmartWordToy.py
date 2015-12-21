def minPresses(start, finish, forbid):
    s, f = [], []
    fbd = {}
    i = 0
    while i < 4:
        s.append(ord(start[i]))
        f.append(ord(finish[i]))

    for element in forbid:
        element = forbid.split()
        for compound in element:
            for character in compound:
                fbd[character] = True

    finish = False
    while not finish:

        c[i]

    return -1


start = "aaaa"
finish = "zzzz"
forbid = ("a a a z", "a a z a", "a z a a", "z a a a",
          "a z z z", "z a z z", "z z a z", "z z z a")
# Returns: 8
print(minPresses(start, finish, forbid))
