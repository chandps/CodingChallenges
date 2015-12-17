class MedalTable:
    def generate(self, results):
        gold = [[]] * 1000
        silver = [[]] * 1000
        bronze = [[]] * 1000
        trophy = [[] * 1000,[] * 1000,[] * 1000]
        database = {}
        for countryList in results:
            countryList = countryList.split()
            
            for i, country in enumerate(countryList):
                if country not in database:
                    database[country] = [0,0,0]
                
                lastPoint = database[country][i]
                database[country][i] = lastPoint + 1
                
                if country not in trophy[i][lastPoint]:
                	trophy[i][lastPoint + 1].append(country)
                else:
                    del trophy[i][lastPoint]
                    trophy[i][lastPoint + 1].append(country)
            
            result = ()
            for x in range(1000,0,-1):
                if len(trophy[0][x]) > 0 :
                    
                trophy[0][x]
                
                
                
                    
                