class TallPeople:

    def getPeople(people):
        tallestColumn = [0] * len(people[0].split())
        print(tallestColumn)
        tallestOfShortest = 0
        for row in people:
            shortestRow = 100000
            for columnIndex, height in enumerate(map(int, row.split())):
                if height < shortestRow:
                    shortestRow = height
                if height > tallestColumn[columnIndex]:
                    print(columnIndex)
                    tallestColumn[columnIndex] = height
            if shortestRow > tallestOfShortest:
                tallestOfShortest = shortestRow
        shortest = 100000
        for height in tallestColumn:
            if height < shortest:
                shortest = height
        return (tallestOfShortest, shortest)

    people = ("9 2 3", "4 8 7")
    print(getPeople(people))
