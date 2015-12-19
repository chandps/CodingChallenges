class Country():

    def __init__(self, name, gold, silver, bronze):
        self.name = name
        self.gold, self.silver, self.bronze = gold, silver, bronze

    def __str__(self):
        return "%s %d %d %d" % (self.name, self.gold, self.silver, self.bronze)

    def __lt__(self, other):
        if self.gold == other.gold:
            if self.silver == other.silver:
                if self.bronze == other.bronze:
                    return self.name > other.name
                return self.bronze < other.bronze
            return self.silver < other.silver
        return self.gold < other.gold


class MedalTable:

    def generate(self, results):
        trophy = {}

        for cList in results:
            for i, cname in enumerate(cList.split()):
                if cname not in trophy:
                    trophy[cname] = Country(cname, 0, 0, 0)
                if i == 0:
                    trophy[cname].gold = trophy[cname].gold + 1
                if i == 1:
                    trophy[cname].silver = trophy[cname].silver + 1
                if i == 2:
                    trophy[cname].bronze = trophy[cname].bronze + 1
        trophyList = tuple(trophy.values())

        return sorted(trophyList, reverse=True)
