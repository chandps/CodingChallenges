class MedalTable:

    class country():

        def __init__(self, name, gold, silver, bronze):
            self.name = name
            self.gold, self.silver, self.bronze = gold, silver, bronze

        def __str__(self):
            return "%s %d %d %d" % (self.name, self.gold, self.silver, self.bronze)

        def __lt__(self, other):
            if self.gold == other.gold:
                if self.silver == other.silver:
                    if self.bronze == other.bronze:
                        return self.name < other.name
                    return self.bronze < other.bronze
                return self.silver < other.silver
            return self.gold < other.gold

    data = []
    data.append(country("KOR", 5, 0, 0))
    data.append(country("JPY", 3, 1, 2))
    data.append(country("CHN", 3, 1, 3))
    data.append(country("HKG", 4, 0, 1))

    data.sort()
    for x in data:
        print(x)

"""    def generate(self, results):
        gold = [[]] * 1000
        silver = [[]] * 1000
        bronze = [[]] * 1000
        trophy = [[] * 1000, [] * 1000, [] * 1000]
        database = {}
        for countryList in results:
            countryList = countryList.split()

            for i, country in enumerate(countryList):
                if country not in database:
                    database[country] = [0, 0, 0]

                lastPoint = database[country][i]
                database[country][i] = lastPoint + 1

                if country not in trophy[i][lastPoint]:
                    trophy[i][lastPoint + 1].append(country)
                else:
                    del trophy[i][lastPoint]
                    trophy[i][lastPoint + 1].append(country)

            result = ()
            for x in range(1000, 0, -1):
                if len(trophy[0][x]) > 0:

                trophy[0][x]"""
